import unittest
import os
from main import load_customer_feedback  # Importing from main.py


class TestCustomerFeedback(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the dataset before running tests using the function from main.py
        cls.df = load_customer_feedback()

    def test_file_exists(self):
        # Check if the file exists
        self.assertTrue(
            os.path.exists("data/customer_feedback_satisfaction1.csv"),
            "CSV file does not exist.",
        )

    def test_dataframe_not_empty(self):
        # Ensure the DataFrame is not empty
        self.assertFalse(self.df.empty, "DataFrame is empty.")

    def test_columns_exist(self):
        # Check that specific columns exist in the DataFrame
        expected_columns = [
            "CustomerID",
            "Age",
            "Gender",
            "Country",
            "Income",
            "ProductQuality",
            "ServiceQuality",
            "PurchaseFrequency",
            "FeedbackScore",
            "LoyaltyLevel",
            "SatisfactionScore",
        ]
        for column in expected_columns:
            self.assertIn(
                column, self.df.columns, f"Column {column} is missing in the DataFrame."
            )

    def test_no_null_values(self):
        # Ensure there are no null values in the DataFrame
        self.assertFalse(
            self.df.isnull().values.any(), "DataFrame contains null values."
        )


if __name__ == "__main__":
    unittest.main()
