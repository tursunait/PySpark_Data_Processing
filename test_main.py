import unittest
from unittest.mock import patch, mock_open
import sys
import sqlite3
from main import main
from mylib.transform_load import load


class TestMain(unittest.TestCase):

    @patch("mylib.transform_load.load")
    def test_load_action(self, mock_load):
        # Mock data and arguments that match the customer_feedback_satisfaction schema
        mock_data = (
            "1,25,M,USA,50000,4,5,3,8,Gold,85.5\n"
            "2,30,F,Canada,40000,3,4,2,7,Silver,75.0\n"
        )
        with patch("builtins.open", mock_open(read_data=mock_data)):
            test_args = ["main.py", "load", "--dataset", "test_data.csv"]
            with patch.object(sys, "argv", test_args):
                # Use an in-memory database for testing
                conn = sqlite3.connect(":memory:")
                mock_load.side_effect = lambda dataset, db_connection=conn: load(
                    dataset, db_connection
                )
                main()
                mock_load.assert_called_once_with("test_data.csv", conn)
                conn.close()
