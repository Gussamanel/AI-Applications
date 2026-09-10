"""
Content-Based Movie Recommender System
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module constructs user preference profile vectors based on genre metadata 
and historical ratings, using cosine similarity to generate recommendations.
"""

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    """Content-based recommender engine."""

    def __init__(self, movies_df: pd.DataFrame, ratings_df: pd.DataFrame):
        self.movies_df = movies_df
        self.ratings_df = ratings_df
        self.genre_columns = [col for col in movies_df.columns if "genre_" in col]
        self.movie_features = movies_df.set_index("movie_title")[self.genre_columns]

        user_ratings = pd.melt(
            ratings_df,
            id_vars="User",
            var_name="movie_title",
            value_name="Ratings",
        )
        self.reviews = user_ratings[
            (user_ratings["Ratings"] > 0) & (user_ratings["movie_title"] != "Unnamed: 0")
        ]

    def get_user_profile(self, user_id: str) -> np.ndarray:
        """Computes weighted average genre profile vector for a user."""
        user_rated = self.reviews[self.reviews["User"] == user_id]
        if user_rated.empty:
            return np.zeros(len(self.genre_columns))

        user_selection = pd.merge(
            user_rated, self.movie_features, on="movie_title", how="left"
        )
        user_profile = np.dot(
            user_selection[self.genre_columns].T.fillna(0), user_rated["Ratings"]
        )

        total = user_profile.sum()
        if total > 0:
            user_profile = user_profile / total

        return user_profile

    def generate_recommendations(
        self, user_profile: np.ndarray, num_recommendations: int = 5
    ) -> pd.DataFrame:
        """Ranks candidate movies using Cosine Similarity against user profile vector."""
        user_profile = np.nan_to_num(user_profile.reshape(1, -1))
        features_array = self.movie_features.fillna(0).values

        similarity = cosine_similarity(user_profile, features_array)
        recommendations = pd.DataFrame(
            {
                "movie_title": self.movie_features.index,
                "similarity": similarity.flatten(),
            }
        )

        return recommendations.sort_values(by="similarity", ascending=False).head(
            num_recommendations
        )


def main():
    print("=== Content-Based Movie Recommender System ===")
    try:
        movies_df = pd.read_csv("movie_genres.csv")
        ratings_df = pd.read_csv("user_reviews.csv")

        recommender = MovieRecommender(movies_df, ratings_df)
        users = ["Vincent", "Edgar", "Addilyn", "Marlee", "Javier"]

        for user in users:
            profile = recommender.get_user_profile(user)
            recs = recommender.generate_recommendations(profile, num_recommendations=5)
            print(f"\nTop 5 Recommendations for {user}:")
            print(recs.to_string(index=False))

    except FileNotFoundError as e:
        print(f"Dataset note: Place movie_genres.csv and user_reviews.csv in folder to run demo. ({e})")


if __name__ == "__main__":
    main()
