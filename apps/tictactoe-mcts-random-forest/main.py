"""
Hybrid Tic-Tac-Toe MCTS + Random Forest Agent
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module implements a hybrid Monte Carlo Tree Search agent that integrates 
a trained Random Forest regressor/classifier to evaluate intermediate board states.
"""

import copy
import random
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def convert_board_to_array(board):
    """Converts a 3x3 character board to a 1D numeric feature vector."""
    board_array = np.zeros((3, 3), dtype=int)
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                board_array[row][col] = 1
            elif board[row][col] == 'O':
                board_array[row][col] = -1
    return board_array.flatten()


def extract_partial_states(row):
    """Extracts board state snapshots throughout a recorded game sequence."""
    board = np.zeros((3, 3), dtype=int)
    winner = row["Winner"]
    partial_states = []

    moves = row[1:].values
    for i, move in enumerate(moves):
        if move == "---" or pd.isna(move):
            break
        row_idx, col_idx = map(int, str(move).split("-"))
        player = 1 if i % 2 == 0 else -1
        board[row_idx, col_idx] = player
        partial_states.append((board.flatten().tolist(), winner))

    return partial_states


def process_data(df):
    """Processes historical game data into training matrices X and y."""
    all_data = []
    for _, row in df.iterrows():
        all_data.extend(extract_partial_states(row))

    expanded_df = pd.DataFrame(all_data, columns=["board_state", "winner"])
    expanded_df["winner"] = expanded_df["winner"].map({"X": 1, "O": -1, "-": 0})

    X = np.vstack(expanded_df["board_state"].values)
    y = expanded_df["winner"].values
    return X, y


class TicTacToe:
    """Tic-Tac-Toe game board logic."""

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_winner(self, player):
        for row in range(3):
            if all(self.board[row][col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(
            self.board[i][2 - i] == player for i in range(3)
        ):
            return True
        return False

    def is_draw(self):
        return all(self.board[r][c] != ' ' for r in range(3) for c in range(3))

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_draw()

    def clone(self):
        new_game = TicTacToe()
        new_game.board = copy.deepcopy(self.board)
        new_game.current_player = self.current_player
        return new_game


class MCTSNode:
    """MCTS Node integrating Random Forest evaluation weights."""

    def __init__(self, game, parent=None, model=None, ratio=0.0, player=1):
        self.game = game
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.model = model
        self.ratio = ratio
        self.random_forest_probability = 0.0
        self.player = player

    def compute_random_forest_prob(self):
        if self.model is None:
            return 0.0
        arr = [convert_board_to_array(self.game.board)]
        probabilities = np.clip(self.model.predict_proba(arr), 1e-10, 1)
        win_prob = probabilities[0][1] if self.player == 1 else probabilities[0][2]
        return win_prob * 10.0

    def is_fully_expanded(self):
        return len(self.children) == len(self.game.available_moves())

    def best_child(self, exploration_weight=1.0):
        return max(
            self.children,
            key=lambda child: (child.wins / (child.visits + 1e-6))
            + exploration_weight
            * (
                (2 * (child.parent.visits + 1) / (child.visits + 1)) ** 0.5 * (1 - child.ratio)
                + child.random_forest_probability * child.ratio
            ),
        )

    def backpropagate(self, result):
        if self.visits < 1 and self.model:
            self.random_forest_probability = self.compute_random_forest_prob()
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(1 - result)

    def expand(self):
        tried_boards = [child.game.board for child in self.children]
        for move in self.game.available_moves():
            new_game = self.game.clone()
            new_game.make_move(*move)
            if new_game.board not in tried_boards:
                child = MCTSNode(
                    new_game,
                    parent=self,
                    model=self.model,
                    ratio=self.ratio,
                    player=self.player,
                )
                self.children.append(child)
                return child
        return None

    def simulate(self):
        sim_game = self.game.clone()
        while not sim_game.is_game_over():
            moves = sim_game.available_moves()
            row, col = random.choice(moves)
            sim_game.make_move(row, col)
        if sim_game.is_winner('X'):
            return 1
        elif sim_game.is_winner('O'):
            return 0
        return 0.5


class MCTS:
    """MCTS Search Engine."""

    def __init__(
        self,
        game,
        iterations=1000,
        model=None,
        ratio=0.0,
        exploration_weight=1.0,
        player=1,
    ):
        self.root = MCTSNode(game, model=model, ratio=ratio, player=player)
        self.iterations = iterations
        self.exploration_weight = exploration_weight

    def best_move(self):
        for _ in range(self.iterations):
            node = self.select()
            if not node.game.is_game_over():
                node = node.expand()
                if node:
                    result = node.simulate()
                    node.backpropagate(result)
        return self.root.best_child(self.exploration_weight).game

    def select(self):
        node = self.root
        while node.is_fully_expanded() and node.children:
            node = node.best_child(self.exploration_weight)
        return node


def play_demo_game(model=None, ratio=0.5):
    game = TicTacToe()
    while not game.is_game_over():
        mcts = MCTS(game, iterations=200, model=model, ratio=ratio)
        game = mcts.best_move()
    print("Demo Game Finished. Final Board:")
    for r in game.board:
        print(r)


if __name__ == "__main__":
    print("=== Hybrid MCTS + Random Forest Agent ===")
    try:
        games_df = pd.read_csv('tictactoe_games.csv')
        X, y = process_data(games_df)
        rf = RandomForestClassifier(random_state=0)
        rf.fit(X, y)
        joblib.dump(rf, "random_forest_tictactoe.pkl")
        print("Trained Random Forest model successfully.")
        play_demo_game(model=rf, ratio=0.5)
    except FileNotFoundError:
        print("Dataset note: Run standalone MCTS demo (place tictactoe_games.csv to enable RF training).")
        play_demo_game(model=None, ratio=0.0)
