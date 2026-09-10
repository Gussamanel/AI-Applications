# 🤖 AI Applications Portfolio

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C.svg)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![MCTS](https://img.shields.io/badge/Algorithm-MCTS%20%26%20UCT-brightgreen.svg)]()
[![Domain](https://img.shields.io/badge/Focus-Multi--Domain%20AI-purple.svg)]()

Welcome to the **AI Applications Portfolio**. This repository showcases **6 standalone Artificial Intelligence and Machine Learning applications**, spanning Computer Vision, Conversational AI, Game AI, Recommender Systems, and Unsupervised Learning.

Each project explores distinct algorithmic paradigms, dataset challenges, and theoretical models—ranging from PyTorch convolutional neural networks and Monte Carlo Tree Search to custom rule-based NLP engines and spatial distribution shift evaluation.

---

## 🚀 Projects Overview & Navigation

| Icon | Application | Primary Domain | Core Tech Stack | Quick Link |
| :---: | :--- | :--- | :--- | :---: |
| 🛰️ | **GeoTIFF Land-Cover Classifier** | Computer Vision & Geospatial | PyTorch CNNs, Spatial K-Fold, GeoTIFF | [Explore App ➔](apps/geotiff-classifier) |
| 💬 | **Multi-Domain Dialog System** | Conversational AI & NLP | Python, Regex, Pandas, State Machines | [Explore App ➔](apps/dialog-system) |
| 🎲 | **AlphaGo-Inspired MCTS Agent** | Game AI & Tree Search | Python, NumPy, MCTS, UCT Selection | [Explore App ➔](apps/alphago-mcts) |
| 🧠 | **Tic-Tac-Toe MCTS + Random Forest** | Hybrid Machine Learning | Scikit-Learn, MCTS, Random Forest | [Explore App ➔](apps/tictactoe-mcts-random-forest) |
| 🎬 | **Content-Based Movie Recommender** | Recommender Systems | Scikit-Learn, Cosine Similarity, Pandas | [Explore App ➔](apps/movie-recommender) |
| 🌤️ | **Air Quality K-Means Clustering** | Unsupervised Learning | Scikit-Learn, K-Means, Shift Analysis | [Explore App ➔](apps/air-quality-clustering) |

---

## 📌 Detailed Project Breakdown

### 🛰️ 1. GeoTIFF Land-Cover Classifier
* **Domain**: Computer Vision / Remote Sensing & Deep Learning
* **Directory**: [`apps/geotiff-classifier`](apps/geotiff-classifier)
* **Original Report**: [`annotated-Assignment5-1.pdf`](reports/annotated-Assignment5-1.pdf)
* **Summary**: A PyTorch deep learning pipeline designed to classify satellite and aerial land-cover imagery from Potsdam GeoTIFF data. Implements spatial K-fold cross-validation to prevent geographic data leakage between training and validation splits.
* **Key Techniques**: PyTorch CNN architectures, spatial cross-validation, multi-spectral tensor processing, land-cover semantic categorization.

---

### 💬 2. Multi-Domain Dialog System
* **Domain**: Natural Language Processing / Conversational AI
* **Directory**: [`apps/dialog-system`](apps/dialog-system)
* **Original Report**: [`annotated-vertopal.com_Final_A6.pdf`](reports/annotated-vertopal.com_Final_A6.pdf)
* **Summary**: A multi-intent rule-based conversational assistant capable of managing session state across three distinct domains: restaurant recommendations, flight bookings, and weather reports.
* **Key Techniques**: Keyword & entity extraction regex, stateful slot-filling, Pandas query generation, multi-domain conversation management.

---

### 🎲 3. AlphaGo-Inspired MCTS Agent
* **Domain**: Game AI / Reinforcement Learning & Search
* **Directory**: [`apps/alphago-mcts`](apps/alphago-mcts)
* **Original Report**: [`annotated-Module3-1.pdf`](reports/annotated-Module3-1.pdf)
* **Summary**: A game-playing agent inspired by AlphaGo that implements Monte Carlo Tree Search (MCTS) with the Upper Confidence Bound for Trees (UCT) selection policy. Evaluated on generalized $N \times N$ tic-tac-toe boards under varying simulation budgets.
* **Key Techniques**: MCTS tree policy, UCT exploration/exploitation balance, random rollout evaluation, multi-board size scalability.

---

### 🧠 4. Tic-Tac-Toe MCTS + Random Forest Evaluation
* **Domain**: Hybrid Machine Learning & Game Search
* **Directory**: [`apps/tictactoe-mcts-random-forest`](apps/tictactoe-mcts-random-forest)
* **Original Report**: [`annotated-Final_Report_A8.pdf`](reports/annotated-Final_Report_A8.pdf)
* **Summary**: An advanced hybrid game-playing agent that replaces pure random rollouts in MCTS with state evaluations from a trained Random Forest regressor. Compares combined model performance across different weighting ratios ($w_{MCTS}$ vs $w_{RF}$).
* **Key Techniques**: Feature extraction from partial game boards, Scikit-Learn Random Forest regression, hybrid MCTS evaluation, heuristic tuning.

---

### 🎬 5. Content-Based Movie Recommender
* **Domain**: Information Retrieval & Recommender Systems
* **Directory**: [`apps/movie-recommender`](apps/movie-recommender)
* **Original Report**: [`annotated-Module%202.pdf`](reports/annotated-Module%202.pdf)
* **Summary**: A personalized recommendation engine that constructs weighted user preference vectors based on historical movie ratings and genre features, using cosine similarity to rank unwatched items.
* **Key Techniques**: Genre feature vector representation, user profile weighting, vector space cosine similarity scoring, candidate ranking.

---

### 🌤️ 6. Air Quality K-Means Clustering & Distribution Shift
* **Domain**: Unsupervised Learning & ML Reliability
* **Directory**: [`apps/air-quality-clustering`](apps/air-quality-clustering)
* **Original Report**: [`annotated-Assignment7.pdf`](reports/annotated-Assignment7.pdf)
* **Summary**: An unsupervised clustering study analyzing air pollution dataset shifts. The model is trained on data from northern cities (Beijing & Shenyang) and evaluated on southern cities (Guangzhou & Shanghai) to study environmental distribution shifts and model generalization.
* **Key Techniques**: K-Means clustering, dataset shift analysis, silhouette/inertia metrics, cross-city model robustness evaluation.

---

## 📂 Repository Structure & Navigation

```text
AI-Applications/
├── README.md                           # Main Portfolio Landing Page & Architecture Map
├── apps/                               # Source code & individual project documentation
│   ├── geotiff-classifier/             # App 1: PyTorch Satellite Imagery Classifier
│   ├── dialog-system/                  # App 2: Stateful Conversational Assistant
│   ├── alphago-mcts/                   # App 3: AlphaGo MCTS Game Engine
│   ├── tictactoe-mcts-random-forest/   # App 4: Hybrid MCTS + Random Forest Agent
│   ├── movie-recommender/              # App 5: Vector Space Movie Recommender
│   └── air-quality-clustering/         # App 6: Air Quality Clustering & Shift Evaluator
└── reports/                            # Original annotated academic research reports (PDFs)
```

Each application subfolder in `apps/` contains:
- `README.md`: Standalone project documentation, algorithm explanation, and tech stack details.
- `source-listing.md`: Page-labeled Python source code extraction from the project report.
- `report-extracted.txt`: Complete searchable text extraction of the report.

*Note: The original PDFs in [`reports/`](reports) serve as the authoritative baseline documentation.*

---

## 👥 Authors & Academic Context

* **Authors**: Elias Samantzis & Emrik Dunvald (Group 65)
* **Coursework**: Applied Data Science / Artificial Intelligence Applications
