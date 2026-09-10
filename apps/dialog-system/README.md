# 💬 Multi-Domain Conversational Dialog System

[![Domain](https://img.shields.io/badge/Domain-Conversational%20AI-purple.svg)]()
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Pandas%20%7C%20Regex-blue.svg)]()

[⬅ Back to Main Portfolio](../../README.md)

## 📌 Overview
A multi-intent rule-based conversational dialog manager that provides assistance across three separate domains: restaurant search, flight bookings, and weather forecasts. The system manages dialogue session state, handles multi-turn slot filling, and queries structured dataframes to satisfy user requests.

## 🛠️ Tech Stack & Methodology
- **Core Logic**: Python, Regular Expressions (`re`) for intent recognition and entity extraction
- **Data Retrieval**: `pandas` dataframe filtering and conditional querying
- **Dialogue Engine**: Finite State Machine handling session context, entity verification, and fallback prompts

## 📁 Folder Contents
- [`source-listing.md`](source-listing.md): Extracted Python code cells (pages 6-17)
- [`report-extracted.txt`](report-extracted.txt): Full searchable text of the report
- **Original PDF**: [`reports/annotated-vertopal.com_Final_A6.pdf`](../../reports/annotated-vertopal.com_Final_A6.pdf)

## ⚡ Data & Dependencies
- **Dependencies**: `pandas`, `numpy`
- **Data Note**: Queries local CSV dataframes for restaurants, flight schedules, and weather reports. Ensure dataset paths match local environment before execution.
