import pandas as pd
import os


def extract(file_path="data/customer_feedback_satisfaction1.csv"):
    """Loads a local CSV file and returns the DataFrame."""

    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Load the dataset
    df = pd.read_csv(file_path)

    return df


if __name__ == "__main__":
    df = extract()
    print(df)
