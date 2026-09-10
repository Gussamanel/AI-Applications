# 🌤️ Air Quality K-Means Clustering & Shift Analysis

[![Domain](https://img.shields.io/badge/Domain-Unsupervised%20Learning-teal.svg)]()
[![Topic](https://img.shields.io/badge/Topic-Dataset%20Distribution%20Shift-red.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
An unsupervised machine learning research project evaluating K-Means clustering performance and dataset distribution shift. The model is trained on air quality measurements from northern Chinese cities (Beijing & Shenyang) and tested on southern cities (Guangzhou & Shanghai) to analyze cross-geographic generalization and model stability.

## 🛠️ Tech Stack & Methodology
- **Clustering Algorithm**: Scikit-Learn `KMeans`
- **Feature Processing**: Normalization and multi-pollutant feature matrix scaling
- **Evaluation**: Inertia, silhouette score comparison across training vs. out-of-distribution evaluation cities

## 📁 Folder Contents
- [`source-listing.md`](source-listing.md): Extracted Python code cells (pages 3-6)
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the report
- **Original PDF**: [`reports/annotated-Assignment7.pdf`](../../reports/annotated-Assignment7.pdf)

## ⚡ Data & Dependencies
- **Dependencies**: `scikit-learn`, `pandas`, `numpy`, `matplotlib`
- **Data Note**: Expects `Beijing_labeled.csv`, `Shenyang_labeled.csv`, `Guangzhou_labeled.csv`, and `Shanghai_labeled.csv`.
