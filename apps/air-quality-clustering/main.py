"""
Air-Quality K-Means Clustering & Distribution Shift Analysis
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module implements a custom K-Means classifier to study environmental data 
clustering and evaluate performance across out-of-distribution geographical regions.
"""

import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class KmeansClassifier:
    """Custom K-Means classifier supporting multi-start initialization."""

    def __init__(self, k: int = 8, max_iter: int = 50, random_inits: int = 10):
        self.k = k
        self.max_iter = max_iter
        self.random_inits = random_inits
        self.clusters = []
        self.cluster_labels = []
        self.cluster_centers = []

    def fit(self, X: pd.DataFrame, y: pd.Series):
        targets = y.to_numpy()
        features = X.to_numpy()
        best_sse = np.inf

        for _ in range(self.random_inits):
            init_indices = random.sample(range(len(features)), self.k)
            cluster_centers = [features[i].copy() for i in init_indices]

            for _ in range(self.max_iter):
                clusters = [[] for _ in range(self.k)]
                cluster_labels = [[] for _ in range(self.k)]

                for target, feature in zip(targets, features):
                    dists = [np.linalg.norm(feature - center) for center in cluster_centers]
                    index = int(np.argmin(dists))
                    clusters[index].append(feature)
                    cluster_labels[index].append(target)

                for n in range(self.k):
                    if len(clusters[n]) > 0:
                        cluster_centers[n] = np.mean(clusters[n], axis=0)

            clusterwise_sse = 0.0
            for centroid, points in zip(cluster_centers, clusters):
                if len(points) > 0:
                    sse = sum([np.sum(np.square(centroid - p)) for p in points])
                    clusterwise_sse += sse

            if clusterwise_sse < best_sse:
                best_sse = clusterwise_sse
                self.clusters = clusters
                self.cluster_centers = cluster_centers

                self.cluster_labels = []
                for labels in cluster_labels:
                    if len(labels) > 0:
                        avg_label = sum(labels) / len(labels)
                        self.cluster_labels.append(round(avg_label))
                    else:
                        self.cluster_labels.append(0)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        predictions = []
        features = X.to_numpy()
        for feature in features:
            dists = [np.linalg.norm(feature - center) for center in self.cluster_centers]
            index = int(np.argmin(dists))
            predictions.append(self.cluster_labels[index])
        return np.array(predictions)

    def accuracy(self, y_pred: np.ndarray, y_true: pd.Series) -> float:
        pred = np.asarray(y_pred)
        true = np.asarray(y_true)
        return float(np.average(np.equal(pred, true)))


def main():
    print("=== Air-Quality K-Means Clustering Experiment ===")
    try:
        beijing = pd.read_csv("Beijing_labeled.csv")
        shenyang = pd.read_csv("Shenyang_labeled.csv")
        combined = pd.concat([beijing, shenyang], ignore_index=True)

        y = combined["PM_HIGH"]
        X = combined.drop(columns=["PM_HIGH"])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

        kms = KmeansClassifier(k=8, max_iter=50, random_inits=10)
        kms.fit(X_train, y_train)

        prediction = kms.predict(X_test)
        ac = kms.accuracy(prediction, y_test)
        print(f"Beijing/Shenyang Validation Accuracy: {ac:.4f}")

        guangzhou = pd.read_csv("Guangzhou_labeled.csv")
        shanghai = pd.read_csv("Shanghai_labeled.csv")
        test_df = pd.concat([guangzhou, shanghai], ignore_index=True)

        y_out = test_df["PM_HIGH"]
        X_out = test_df.drop(columns=["PM_HIGH"])

        out_prediction = kms.predict(X_out)
        out_ac = kms.accuracy(out_prediction, y_out)
        print(f"Guangzhou/Shanghai Out-Of-Distribution Accuracy: {out_ac:.4f}")

    except FileNotFoundError as e:
        print(f"Data Note: Place dataset CSV files in folder to execute full pipeline. ({e})")


if __name__ == "__main__":
    main()
