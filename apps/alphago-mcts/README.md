# 🎲 AlphaGo-Inspired Monte Carlo Tree Search (MCTS)

[![Domain](https://img.shields.io/badge/Domain-Game%20AI%20%26%20Search-red.svg)]()
[![Algorithm](https://img.shields.io/badge/Algorithm-MCTS%20%2B%20UCT-brightgreen.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
A game-playing agent inspired by AlphaGo's tree search mechanism. It implements Monte Carlo Tree Search (MCTS) utilizing the Upper Confidence Bound for Trees (UCT) selection policy to determine optimal moves in generalized tic-tac-toe games across varying board dimensions and simulation iteration budgets.

## 🛠️ Tech Stack & Methodology
- **Algorithm**: Monte Carlo Tree Search (Selection, Expansion, Simulation/Rollout, Backpropagation)
- **Selection Policy**: UCT (Upper Confidence Bound applied to Trees) formula balancing exploitation of high-win nodes and exploration of unvisited nodes
- **Language & Libraries**: Pure Python, `numpy` matrix calculations

## 📁 Folder Contents
- [`source-listing.md`](source-listing.md): Extracted Python code cells (pages 1-10)
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the report
- **Original PDF**: [`reports/annotated-Module3-1.pdf`](../../reports/annotated-Module3-1.pdf)

## ⚡ Data & Dependencies
- **Dependencies**: `numpy`, Python Standard Library
- **Self-Contained**: Requires no external datasets; runs directly as an interactive game simulation or benchmark script.
