import unittest
from unittest.mock import patch, MagicMock
from main import main


class TestMain(unittest.TestCase):
    @patch("main.set_pyspark_python_env")
    @patch("main.start_spark")
    @patch("main.read_csv")
    @patch("main.show_data")
    @patch("main.show_summary_stats")
    @patch("main.calculate_avg_satisfaction_by_country")
    @patch("main.plot_corr_matrix")
    @patch("main.plot_satisfaction_distribution")
    @patch("main.end_spark")
    def test_main(
        self,
        mock_end_spark,
        mock_plot_satisfaction_distribution,
        mock_plot_corr_matrix,
        mock_calculate_avg_satisfaction,
        mock_show_summary_stats,
        mock_show_data,
        mock_read_csv,
        mock_start_spark,
        mock_set_pyspark_python_env,
    ):
        # Set up mocks for return values
        mock_spark = MagicMock()
        mock_df = MagicMock()
        mock_start_spark.return_value = mock_spark
        mock_read_csv.return_value = mock_df

        # Run the main function
        main()

        # Assert that each function is called as expected
        mock_set_pyspark_python_env.assert_called_once_with("python3")
        mock_start_spark.assert_called_once_with("CustomerFeedbackAnalysis")
        mock_read_csv.assert_called_once_with(
            mock_spark, "data/customer_feedback_satisfaction.csv"
        )
        mock_df.createOrReplaceTempView.assert_called_once_with("customer_feedback")
        mock_show_data.assert_called_once_with(mock_df)
        mock_show_summary_stats.assert_called_once_with(
            mock_df, ["Age", "Income", "PurchaseFrequency", "SatisfactionScore"]
        )
        mock_calculate_avg_satisfaction.assert_called_once_with(mock_spark)
        mock_plot_corr_matrix.assert_called_once_with(
            mock_df,
            [
                "Income",
                "ProductQuality",
                "ServiceQuality",
                "PurchaseFrequency",
                "SatisfactionScore",
            ],
        )
        mock_plot_satisfaction_distribution.assert_called_once_with(mock_df)
        mock_end_spark.assert_called_once_with(mock_spark)


if __name__ == "__main__":
    unittest.main()
