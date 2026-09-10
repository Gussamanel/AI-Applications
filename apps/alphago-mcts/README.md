# 🎲 AlphaGo-Inspired Monte Carlo Tree Search (MCTS)

[![Domain](https://img.shields.io/badge/Domain-Game%20AI%20%26%20Search-red.svg)]()
[![Algorithm](https://img.shields.io/badge/Algorithm-MCTS%20%2B%20UCT-brightgreen.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
A game-playing agent inspired by AlphaGo's tree search mechanism. It implements Monte Carlo Tree Search (MCTS) utilizing the Upper Confidence Bound for Trees (UCT) selection policy to determine optimal moves in generalized tic-tac-toe games across varying board dimensions and simulation iteration budgets.

## 🛠️ Tech Stack & Methodology
- **Algorithm**: Monte Carlo Tree Search (Selection, Expansion, Simulation/Rollout, Backpropagation)
- **Selection Policy**: UCT (Upper Confidence Bound applied to Trees) formula balancing exploitation of high-win nodes and exploration of unvisited nodes
- **Language & Libraries**: Pure Python, `numpy`, `pandas`

## 📁 Files & Structure
- [`main.py`](main.py): Clean, standalone Python executable code file.
- [`source-listing.md`](source-listing.md): Extracted Python source code with syntax highlighting.
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the original report.
- **Original PDF**: [`reports/annotated-Module3-1.pdf`](../../reports/annotated-Module3-1.pdf)

## ⚡ Execution & Dependencies
```bash
python main.py
```
- **Dependencies**: `pandas`, `numpy`, Python Standard Library
