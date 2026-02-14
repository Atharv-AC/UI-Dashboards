import os
import pandas as pd
import sqlite3
import streamlit as st

BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "..", "Dataset", "StudentsPerformance_cleaned.csv")

# Database stored in writable runtime directory
DB_PATH = "Performance.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


@st.cache_data
def load_csv():
    df = pd.read_csv(csv_path)

    df["total_score"] = (
        df["math_score"] +
        df["reading_score"] +
        df["writing_score"]
    )

    # Write to SQLite
    conn = get_connection()
    df.to_sql("Students", conn, if_exists="replace", index=False)
    conn.close()

    return df
