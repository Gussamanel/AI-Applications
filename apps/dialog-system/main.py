"""
Multi-Domain Conversational Assistant
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module implements a rule-based multi-turn conversational dialogue system 
for restaurant search, flight bookings, and weather queries.
"""

import re
import pandas as pd
from dateutil import parser


class TaskManager:
    """Database query engine for dialogue requests."""

    def __init__(self, weather_df=None, restaurant_df=None, travel_df=None):
        self.weather_df = weather_df
        self.restaurant_df = restaurant_df
        self.travel_df = travel_df

    def query_weather(self, location, date, search_parameters):
        params = [p for p in search_parameters if p not in ['location', 'date']]
        results = {}
        if self.weather_df is None:
            return {p: None for p in params}

        for param in params:
            try:
                sub = self.weather_df.loc[
                    (self.weather_df['Location'] == location)
                    & (pd.to_datetime(self.weather_df["Date_Time"]).dt.date == pd.to_datetime(date).date()),
                    param,
                ].reset_index(drop=True)
                results[param] = sub.iloc[0] if not sub.empty else None
            except Exception:
                results[param] = None
        return results

    def query_restaurant(self, city, cuisines, search_parameters):
        params = [p for p in search_parameters if p not in ['city', 'cuisines']]
        results = {}
        if self.restaurant_df is None:
            return {p: None for p in params}

        for param in params:
            try:
                sub = self.restaurant_df.loc[
                    (self.restaurant_df['city'].str.lower() == city.lower())
                    & (self.restaurant_df['cuisines'].str.contains(cuisines, case=False, na=False)),
                    param,
                ].reset_index(drop=True)
                results[param] = sub.iloc[0] if not sub.empty else None
            except Exception:
                results[param] = None
        return results

    def query_travel(self, search_parameters):
        if self.travel_df is None:
            return pd.DataFrame()
        date = search_parameters.get('date')
        df = self.travel_df.loc[
            pd.to_datetime(self.travel_df["date"], dayfirst=True).dt.date == pd.to_datetime(date).date()
        ]
        params = {k: v for k, v in search_parameters.items() if k != 'date' and v is not None}
        for param, value in params.items():
            df = df[df[param] == value]
        return df


class ChatBoxUtility:
    """NLTK and Regex parser helper utility."""

    def extract_main_topic(self, user_tokens, main_topics_dict):
        for topic, keywords in main_topics_dict.items():
            if user_tokens.intersection(keywords):
                return topic
        return None

    def extract_date(self, user_input):
        try:
            date = parser.parse(user_input, fuzzy=True)
            return date.strftime("%Y-%m-%d")
        except Exception:
            return None

    def format_date_natural(self, date_str):
        date_obj = pd.to_datetime(date_str)
        day = date_obj.day
        suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return f"{day}{suffix} of {date_obj.strftime('%B %Y')}"

    def extract_destination(self, query):
        departure = re.search(r"\b(?:from) ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)", query)
        destination = re.search(r"\b(?:to) ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)", query)
        dep = departure.group(1) if departure else None
        dest = destination.group(1) if destination else None
        return dep, dest


class MultiDomainChatBot(ChatBoxUtility):
    """Main Dialogue Assistant."""

    def __init__(self, weather_df=None, restaurant_df=None, travel_df=None):
        super().__init__()
        self.task_manager = TaskManager(weather_df, restaurant_df, travel_df)
        self.main_topics = {
            'weather': {'weather', 'temperature', 'cold', 'warm', 'hot'},
            'restaurant': {'food', 'restaurant', 'eat', 'drink', 'hungry'},
            'travel': {'travel', 'flight', 'trip', 'airline', 'fly'},
        }

    def process_query(self, query: str) -> str:
        tokens = set(query.lower().split())
        topic = self.extract_main_topic(tokens, self.main_topics)

        if topic == 'weather':
            return f"Processing weather query for input: '{query}'"
        elif topic == 'restaurant':
            return f"Processing restaurant recommendation for input: '{query}'"
        elif topic == 'travel':
            return f"Processing flight travel booking for input: '{query}'"
        else:
            return "I can assist with weather reports, restaurant search, or flight bookings. Could you specify?"


if __name__ == '__main__':
    print("=== Multi-Domain Conversational Assistant ===")
    bot = MultiDomainChatBot()
    print("Bot Response:", bot.process_query("What is the weather in Delhi tomorrow?"))
