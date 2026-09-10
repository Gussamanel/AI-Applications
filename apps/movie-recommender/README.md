# 🎬 Content-Based Movie Recommender System

[![Domain](https://img.shields.io/badge/Domain-Recommender%20Systems-green.svg)]()
[![Metric](https://img.shields.io/badge/Metric-Cosine%20Similarity-blue.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
A personalized content-based recommendation system that analyzes movie genre metadata and user rating histories. The engine builds a weighted profile vector representing the user's genre preferences and ranks candidate movies using cosine similarity metrics in vector space.

## 🛠️ Tech Stack & Methodology
- **Vector Model**: One-hot encoded genre feature vectors for candidate films
- **User Profiling**: Rating-weighted aggregation of genre vectors across watched films
- **Similarity Metric**: Cosine similarity between user profile vector and unrated candidate film vectors
- **Implementation**: Python, `pandas`, `numpy`, `scikit-learn`

## 📁 Files & Structure
- [`main.py`](main.py): Clean, standalone Python executable code file.
- [`source-listing.md`](source-listing.md): Extracted Python source code with syntax highlighting.
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the original report.
- **Original PDF**: [`reports/annotated-Module%202.pdf`](../../reports/annotated-Module%202.pdf)

## ⚡ Execution & Dependencies
```bash
python main.py
```
- **Dependencies**: `pandas`, `numpy`, `scikit-learn`
