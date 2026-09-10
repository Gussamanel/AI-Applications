# 🧠 Hybrid Tic-Tac-Toe: MCTS + Random Forest Evaluation

[![Domain](https://img.shields.io/badge/Domain-Hybrid%20Machine%20Learning-orange.svg)]()
[![Models](https://img.shields.io/badge/Models-MCTS%20%2B%20Random%20Forest-yellow.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
An advanced hybrid game-playing framework combining Monte Carlo Tree Search (MCTS) with machine learning value estimation. Instead of executing full random rollouts to terminal game states, the agent uses a Random Forest Regressor trained on intermediate board positions to evaluate state scores, accelerating search efficiency.

## 🛠️ Tech Stack & Methodology
- **Tree Search**: MCTS tree expansion and node selection
- **ML Estimator**: `scikit-learn` `RandomForestRegressor` trained on extracted board feature representations
- **Evaluation Weighting**: Weighted combinations of MCTS simulation statistics ($w_{MCTS}$) and Random Forest evaluation outputs ($w_{RF}$)

## 📁 Folder Contents
- [`source-listing.md`](source-listing.md): Extracted Python code cells (pages 6-14)
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the report
- **Original PDF**: [`reports/annotated-Final_Report_A8.pdf`](../../reports/annotated-Final_Report_A8.pdf)

## ⚡ Data & Dependencies
- **Dependencies**: `scikit-learn`, `numpy`, `pandas`
- **Data Note**: Trains on generated/saved game state evaluation datasets.
