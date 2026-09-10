# 🌤️ Air Quality K-Means Clustering & Shift Analysis

[![Domain](https://img.shields.io/badge/Domain-Unsupervised%20Learning-teal.svg)]()
[![Topic](https://img.shields.io/badge/Topic-Dataset%20Distribution%20Shift-red.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
An unsupervised machine learning research project evaluating K-Means clustering performance and dataset distribution shift. The model is trained on air quality measurements from northern Chinese cities (Beijing & Shenyang) and tested on southern cities (Guangzhou & Shanghai) to analyze cross-geographic generalization and model stability.

## 🛠️ Tech Stack & Methodology
- **Clustering Algorithm**: Scikit-Learn `KMeans` / Custom `KmeansClassifier`
- **Feature Processing**: Normalization and multi-pollutant feature matrix scaling
- **Evaluation**: Inertia, silhouette score comparison across training vs. out-of-distribution evaluation cities

## 📁 Files & Structure
- [`main.py`](main.py): Clean, standalone Python executable code file.
- [`source-listing.md`](source-listing.md): Extracted Python source code with syntax highlighting.
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the original report.
- **Original PDF**: [`reports/annotated-Assignment7.pdf`](../../reports/annotated-Assignment7.pdf)

## ⚡ Execution & Dependencies
```bash
python main.py
```
- **Dependencies**: `scikit-learn`, `pandas`, `numpy`
