"""
AlphaGo-Inspired Monte Carlo Tree Search (MCTS) Implementation
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module implements a generalized Tic-Tac-Toe game player using MCTS 
with the Upper Confidence Bound for Trees (UCT) selection policy.
"""

import math
import random
import time
import pandas as pd


class Node:
    """Represents a search tree node in MCTS."""

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0

    def is_fully_expanded(self) -> bool:
        """Returns True if node has children for all available legal moves."""
        return len(self.children) == len(self.state.get_legal_moves())

    def best_child(self, exploration_weight: float = 1.4) -> "Node":
        """Selects best child node based on the Upper Confidence Bound (UCT) formula."""
        return max(
            self.children,
            key=lambda node: (node.value / (node.visits + 1e-6))
            + exploration_weight * math.sqrt(math.log(self.visits + 1) / (node.visits + 1e-6)),
        )


def monte_carlo_tree_search(root: Node, iterations: int = 1000) -> Node:
    """Iteratively selects, expands, simulates, and backpropagates to find the optimal move."""
    for _ in range(iterations):
        node = root
        while node.children:
            node = node.best_child()
        if not node.state.is_terminal() and not node.is_fully_expanded():
            node = expand(node)
        result = simulate(node)
        backpropagate(node, result)
    return root.best_child(exploration_weight=1.4)


def expand(node: Node) -> Node:
    """Expands tree by creating a child node for an unvisited legal move."""
    legal_moves = node.state.get_legal_moves()
    unexplored_moves = [
        move for move in legal_moves if move not in [child.state for child in node.children]
    ]
    move = random.choice(unexplored_moves)
    new_state = node.state.apply_move(move)
    child_node = Node(new_state, parent=node)
    node.children.append(child_node)
    return child_node


def simulate(node: Node) -> int:
    """Simulates a random rollout from current node to terminal state."""
    state = node.state.clone()
    while not state.is_terminal():
        legal_moves = state.get_legal_moves()
        for move in legal_moves:
            new_state = state.apply_move(move)
            if new_state.get_result() == state.current_player:
                return state.current_player
        move = random.choice(legal_moves)
        state = state.apply_move(move)
    return state.get_result()


def backpropagate(node: Node, result: int):
    """Backpropagates simulation result up to the root node."""
    curr = node
    while curr is not None:
        curr.visits += 1
        if result == curr.state.current_player:
            curr.value += 1.0
        elif result == 0:
            curr.value += 0.0
        else:
            curr.value -= 1.0
        curr = curr.parent


class TicTacToe:
    """Generalized Tic-Tac-Toe game state implementation."""

    def __init__(self, size: int = 3):
        self.size = size
        self.board = [0] * (size * size)
        self.current_player = 1

    def get_legal_moves(self) -> list:
        return [i for i in range(self.size * self.size) if self.board[i] == 0]

    def apply_move(self, move: int) -> "TicTacToe":
        new_state = TicTacToe(size=self.size)
        new_state.board = self.board[:]
        new_state.board[move] = self.current_player
        new_state.current_player = -self.current_player
        return new_state

    def is_terminal(self) -> bool:
        return self.get_result() is not None

    def get_result(self):
        size = self.size
        board = self.board
        win_length = 3 if size == 3 else (4 if size == 4 else 5)

        for i in range(size):
            for j in range(size - win_length + 1):
                if board[i * size + j] != 0 and all(
                    board[i * size + j] == board[i * size + j + k] for k in range(win_length)
                ):
                    return board[i * size + j]

        for j in range(size):
            for i in range(size - win_length + 1):
                if board[i * size + j] != 0 and all(
                    board[i * size + j] == board[(i + k) * size + j] for k in range(win_length)
                ):
                    return board[i * size + j]

        for i in range(size - win_length + 1):
            for j in range(size - win_length + 1):
                if board[i * size + j] != 0 and all(
                    board[i * size + j] == board[(i + k) * size + (j + k)] for k in range(win_length)
                ):
                    return board[i * size + j]

        for i in range(size - win_length + 1):
            for j in range(win_length - 1, size):
                if board[i * size + j] != 0 and all(
                    board[i * size + j] == board[(i + k) * size + (j - k)] for k in range(win_length)
                ):
                    return board[i * size + j]

        if 0 not in board:
            return 0
        return None

    def clone(self) -> "TicTacToe":
        new_state = TicTacToe(size=self.size)
        new_state.board = self.board[:]
        new_state.current_player = self.current_player
        return new_state


def evaluate_mcts(size: int = 3, iterations: int = 1000, games: int = 100) -> dict:
    """Evaluates MCTS win/loss/draw stats over game simulations."""
    total_time = 0.0
    wins, losses, draws = 0, 0, 0

    for _ in range(games):
        game = TicTacToe(size=size)
        start_time = time.time()
        while not game.is_terminal():
            root = Node(game)
            best_node = monte_carlo_tree_search(root, iterations=iterations)
            game = best_node.state
        total_time += time.time() - start_time
        result = game.get_result()
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            draws += 1

    return {
        "Grid Size": f"{size}x{size}",
        "Iterations per Move": iterations,
        "Games Played": games,
        "Avg Time per Game (s)": total_time / games,
        "Win Rate": wins / games,
        "Loss Rate": losses / games,
        "Draw Rate": draws / games,
    }


if __name__ == "__main__":
    print("Running MCTS Evaluation on 3x3 Board...")
    stats = evaluate_mcts(size=3, iterations=1000, games=10)
    df_stats = pd.DataFrame([stats])
    print(df_stats.to_string(index=False))
