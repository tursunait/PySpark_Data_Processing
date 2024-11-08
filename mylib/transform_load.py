"""
Transforms and Loads data into the local SQLite3 database
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(
    dataset="/Users/tusunaiturumbekova/PySpark_Data_Processing/data/customer_feedback_satisfaction.csv",
):
    """Transforms and Loads data into the local SQLite3 database"""

    # prints the current working directory
    print(f"Current Working Directory: {os.getcwd()}")

    # Check if the dataset file exists
    if not os.path.exists(dataset):
        print(f"Error: The dataset file '{dataset}' was not found.")
        return

    try:
        # Open the CSV file
        with open(dataset, newline="") as csvfile:
            payload = csv.reader(csvfile, delimiter=",")

            # Skip the header row
            next(payload, None)

            # Connect to the SQLite database
            conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
            c = conn.cursor()

            # Drop the existing table if it exists
            c.execute("DROP TABLE IF EXISTS customer_feedback_satisfaction")

            # Create a new table with the required schema
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

            # Commit changes and close the connection
            conn.commit()
            print("Data loaded successfully into 'customer_feedback_satisfaction'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed even if an error occurs
        conn.close()

    return "customer_feedback_satisfaction"
