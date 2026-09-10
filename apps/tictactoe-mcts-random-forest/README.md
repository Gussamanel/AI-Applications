# 🧠 Hybrid Tic-Tac-Toe: MCTS + Random Forest Evaluation

[![Domain](https://img.shields.io/badge/Domain-Hybrid%20Machine%20Learning-orange.svg)]()
[![Models](https://img.shields.io/badge/Models-MCTS%20%2B%20Random%20Forest-yellow.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
An advanced hybrid game-playing framework combining Monte Carlo Tree Search (MCTS) with machine learning value estimation. Instead of executing full random rollouts to terminal game states, the agent uses a Random Forest Regressor trained on intermediate board positions to evaluate state scores, accelerating search efficiency.

## 🛠️ Tech Stack & Methodology
- **Tree Search**: MCTS tree expansion and node selection
- **ML Estimator**: `scikit-learn` `RandomForestClassifier` trained on extracted board feature representations
- **Evaluation Weighting**: Weighted combinations of MCTS simulation statistics ($w_{MCTS}$) and Random Forest evaluation outputs ($w_{RF}$)

## 📁 Files & Structure
- [`main.py`](main.py): Clean, standalone Python executable code file.
- [`source-listing.md`](source-listing.md): Extracted Python source code with syntax highlighting.
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the original report.
- **Original PDF**: [`reports/annotated-Final_Report_A8.pdf`](../../reports/annotated-Final_Report_A8.pdf)

## ⚡ Execution & Dependencies
```bash
python main.py
```
- **Dependencies**: `scikit-learn`, `numpy`, `pandas`, `joblib`, `tqdm`
