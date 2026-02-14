import os 
import atexit as at
import pandas as pd
import sqlite3


BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "..", "Dataset", "StudentsPerformance_cleaned.csv")
db_path = os.path.join(BASE_DIR, "..", "Dataset", "Performance.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()
at.register(conn.close)

# def get_connection():
#     return sqlite3.connect(db_path)

# df = pd.read_csv(csv_path)

# def new_column(row):
#     return row["math_score"] + row["reading_score"] + row["writing_score"]

# df["total_score"] = df.apply(new_column, axis=1) 


def load_csv():
    df = pd.read_csv(csv_path)

    def new_column(row):
        return row["math_score"] + row["reading_score"] + row["writing_score"]
    
    df["total_score"] = df.apply(new_column, axis=1) 

    df.to_sql("Students", conn, if_exists="replace", index=False)  
    
    # Save back to CSV
    df.to_csv(csv_path, index=False)