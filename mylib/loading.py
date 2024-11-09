import sqlite3
import csv
import os


def load(
    dataset="/Users/tusunaiturumbekova/PySpark_Data_Processing/data/customer_feedback_satisfaction.csv",
    db_connection=None,
):
    """Transforms and Loads data into the customer_feedback_satisfaction SQLite3 database"""

    # Use the provided connection or create one if not provided
    conn = db_connection or sqlite3.connect("customer_feedback_satisfactionDB.db")
    try:
        print(os.getcwd())

        with open(dataset, newline="") as csvfile:
            payload = csv.reader(csvfile, delimiter=",")
            next(payload, None)  # Skip the header row if needed

            c = conn.cursor()
            c.execute("DROP TABLE IF EXISTS customer_feedback_satisfaction")
            c.execute(
                """
                CREATE TABLE customer_feedback_satisfaction (
                    CustomerID INTEGER PRIMARY KEY,
                    Age INTEGER,
                    Gender TEXT,
                    Country TEXT,
                    Income REAL,
                    ProductQuality INTEGER,
                    ServiceQuality INTEGER,
                    PurchaseFrequency INTEGER,
                    FeedbackScore INTEGER,
                    LoyaltyLevel TEXT,
                    SatisfactionScore REAL
                )
                """
            )

            # Insert data into the table
            c.executemany(
                """
                INSERT INTO customer_feedback_satisfaction (
                    CustomerID, Age, Gender, Country, Income, ProductQuality, 
                    ServiceQuality, PurchaseFrequency, FeedbackScore, 
                    LoyaltyLevel, SatisfactionScore
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                payload,
            )

            if not db_connection:
                conn.commit()  # Commit only for file-based connections

            print("Data loaded successfully into 'customer_feedback_satisfaction'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if not db_connection:
            conn.close()
