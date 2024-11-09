"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """General query cursor"""
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    cursor.close()
    conn.close()
    log_query(f"{query}")


def read_data():
    """Read all data from customer_feedback_satisfaction table"""
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer_feedback_satisfaction")
    data = c.fetchall()
    log_query("SELECT * FROM customer_feedback_satisfaction;")
    conn.close()
    return data


if "__name__" == "__main__":
    read_data()
    general_query()
