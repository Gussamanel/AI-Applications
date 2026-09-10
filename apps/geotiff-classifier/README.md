# 🛰️ GeoTIFF Land-Cover Classifier

[![Domain](https://img.shields.io/badge/Domain-Computer%20Vision-blue.svg)]()
[![Framework](https://img.shields.io/badge/Framework-PyTorch-EE4C2C.svg)](https://pytorch.org/)
[![Data](https://img.shields.io/badge/Dataset-Potsdam%20GeoTIFF-green.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
An end-to-end PyTorch deep learning pipeline for land-cover classification on Potsdam multi-spectral GeoTIFF satellite/aerial imagery. This project focuses on evaluating model generalization across spatial boundaries using custom Spatial K-Fold cross-validation to prevent spatial autocorrelation data leakage.

## 🛠️ Tech Stack & Methodology
- **Framework**: PyTorch (`torch`, `torchvision`)
- **Architecture**: Custom Convolutional Neural Network (CNN) variants
- **Validation Strategy**: Spatial K-Fold cross-validation (splitting train/val tiles by geographic coordinates rather than random sampling)
- **Data Format**: Multi-channel GeoTIFF tensors

## 📁 Files & Structure
- [`main.py`](main.py): Clean, standalone Python executable code file.
- [`source-listing.md`](source-listing.md): Extracted Python source code with syntax highlighting.
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the original report.
- **Original PDF**: [`reports/annotated-Assignment5-1.pdf`](../../reports/annotated-Assignment5-1.pdf)

## ⚡ Execution & Dependencies
```bash
python main.py
```
- **Dependencies**: `torch`, `torchvision`, `numpy`, `rasterio` (optional), `scikit-learn`
- **Data Note**: Expects Potsdam GeoTIFF dataset tiles (`Potsdam-GeoTif/*.tif`).
