# main.py

from pyspark_lib import (
    set_pyspark_python_env,
    start_spark,
    read_csv,
    show_data,
    show_summary_stats,
    calculate_avg_satisfaction_by_country,
    plot_corr_matrix,
    plot_satisfaction_distribution,
    end_spark,
)


def main():
    # Set the Python path for PySpark
    set_pyspark_python_env("python3")

    # Start Spark session
    spark = start_spark("CustomerFeedbackAnalysis")

    # Load CSV data
    file_path = "data/customer_feedback_satisfaction.csv"
    df = read_csv(spark, file_path)

    # Register DataFrame as a SQL view
    df.createOrReplaceTempView("customer_feedback")

    # Show data and summary statistics
    show_data(df)
    show_summary_stats(df, ["Age", "Income", "PurchaseFrequency", "SatisfactionScore"])

    # Calculate and show average satisfaction by country
    calculate_avg_satisfaction_by_country(spark)

    # Plot correlation matrix and satisfaction distribution
    plot_corr_matrix(
        df,
        [
            "Income",
            "ProductQuality",
            "ServiceQuality",
            "PurchaseFrequency",
            "SatisfactionScore",
        ],
    )
    plot_satisfaction_distribution(df)

    # End Spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
