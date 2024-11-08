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


def create_rec(
    customer_id,
    age,
    gender,
    country,
    income,
    product_quality,
    service_quality,
    purchase_frequency,
    feedback_score,
    loyalty_level,
    satisfaction_score,
):
    """Inserts a record into the customer_feedback_satisfaction table"""
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO customer_feedback_satisfaction
        (CustomerID, Age, Gender, Country, Income, ProductQuality, 
         ServiceQuality, PurchaseFrequency, FeedbackScore, LoyaltyLevel, SatisfactionScore) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            customer_id,
            age,
            gender,
            country,
            income,
            product_quality,
            service_quality,
            purchase_frequency,
            feedback_score,
            loyalty_level,
            satisfaction_score,
        ),
    )
    conn.commit()
    conn.close()


def update_rec(
    customer_id,
    age,
    gender,
    country,
    income,
    product_quality,
    service_quality,
    purchase_frequency,
    feedback_score,
    loyalty_level,
    satisfaction_score,
):
    """Updates a record based on CustomerID"""
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE customer_feedback_satisfaction
        SET Age = ?, Gender = ?, Country = ?, Income = ?, ProductQuality = ?, 
            ServiceQuality = ?, PurchaseFrequency = ?, FeedbackScore = ?, 
            LoyaltyLevel = ?, SatisfactionScore = ?
        WHERE CustomerID = ?
        """,
        (
            age,
            gender,
            country,
            income,
            product_quality,
            service_quality,
            purchase_frequency,
            feedback_score,
            loyalty_level,
            satisfaction_score,
            customer_id,
        ),
    )
    conn.commit()
    conn.close()

    log_query(
        f"""
        UPDATE customer_feedback_satisfaction SET 
            Age={age}, Gender='{gender}', Country='{country}', Income={income}, 
            ProductQuality={product_quality}, ServiceQuality={service_quality}, 
            PurchaseFrequency={purchase_frequency}, FeedbackScore={feedback_score}, 
            LoyaltyLevel='{loyalty_level}', SatisfactionScore={satisfaction_score} 
        WHERE CustomerID={customer_id};
        """
    )


def read_data():
    """Read all data from customer_feedback_satisfaction table"""
    conn = sqlite3.connect("customer_feedback_satisfactionDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM customer_feedback_satisfaction")
    data = c.fetchall()
    log_query("SELECT * FROM customer_feedback_satisfaction;")
    conn.close()
    return data
