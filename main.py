# main.py
import pandas as pd


def load_customer_feedback(file_path="data/customer_feedback_satisfaction1.csv"):
    # Load and return the DataFrame
    return pd.read_csv(file_path)


if __name__ == "__main__":
    df = load_customer_feedback()
    print(df)
