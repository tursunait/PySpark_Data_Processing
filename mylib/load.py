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
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS customer_feedback_satisfactionDB")
    c.execute(
        "CREATE TABLE customer_feedback_satisfactionDB (CustomerID,Age,Gender,Country,Income,ProductQuality,ServiceQuality,PurchaseFrequency,FeedbackScore,LoyaltyLevel,SatisfactionScore)"
    )
    # insert
    c.executemany(
        "INSERT INTO customer_feedback_satisfactionDB VALUES (?,?, ?, ?, ?, ?, ?, ?,?,?,?)",
        payload,
    )
    conn.commit()
    conn.close()
    return "customer_feedback_satisfactionDB"
