import os
import seaborn as sns
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession, DataFrame

LOG_FILE = "output_log.md"
PLOT_DIR = "plots"  # Directory to save plots

# Ensure plot directory exists
os.makedirs(PLOT_DIR, exist_ok=True)


def log_output(operation, output=None, image_path=None, query=None):
    """Adds to a markdown file with optional image references."""
    with open(LOG_FILE, "a") as file:
        file.write(f"## Operation: {operation}\n\n")
        if query:
            file.write(f"**Query:**\n```\n{query}\n```\n\n")
        if output:
            file.write("**Output:**\n")
            file.write(f"{output}\n\n")
        if image_path:
            file.write(f"![{operation}]({image_path})\n\n")


def plot_corr_matrix(df: DataFrame, columns: list):
    """Plot a correlation matrix for the specified numerical columns."""
    correlation_df = df.select(columns).toPandas().corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_df, annot=True, cmap="coolwarm", center=0)
    plt.title("Correlation Matrix of Customer Feedback Factors")
    image_path = os.path.join(PLOT_DIR, "correlation_matrix.png")
    plt.savefig(image_path)  # Save figure
    plt.close()
    log_output("Plot Correlation Matrix", "Correlation matrix plot saved.", image_path)


def set_pyspark_python_env(python_path="python3"):
    """Set the environment variable for PySpark Python path."""
    os.environ["PYSPARK_PYTHON"] = python_path


def start_spark(app_name="CustomerFeedbackAnalysis") -> SparkSession:
    """Initialize a Spark session with the specified app name."""
    return SparkSession.builder.master("local[*]").appName(app_name).getOrCreate()


def read_csv(session: SparkSession, file_path: str) -> DataFrame:
    """Load a CSV file into a Spark DataFrame."""
    df = (
        session.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(file_path)
    )
    # Capture first few rows for logging
    output = df.limit(5).toPandas().to_markdown()
    log_output(
        "Read CSV", f"Loaded data from {file_path}. Showing first few rows:\n{output}"
    )
    return df


def show_data(df: DataFrame):
    """Display data from DataFrame to verify loading."""
    output = df.limit(5).toPandas().to_markdown()
    log_output("Show Data", output)


def show_summary_stats(df: DataFrame, columns: list):
    """Display summary statistics for specific numerical columns."""
    summary = df.describe(columns).toPandas().to_markdown()
    log_output("Summary Statistics", summary)


def calculate_avg_satisfaction_by_country(spark: SparkSession):
    """Calculate the average satisfaction score by country."""
    query = """
        SELECT Country, AVG(SatisfactionScore) AS Avg_Satisfaction
        FROM customer_feedback
        GROUP BY Country
        ORDER BY Avg_Satisfaction DESC
    """
    avg_satisfaction = spark.sql(query)
    output = avg_satisfaction.toPandas().to_markdown()
    log_output("Average Satisfaction by Country", output, query=query)
    avg_satisfaction.show()


def plot_satisfaction_distribution(df: DataFrame):
    """Plot a histogram for satisfaction scores."""
    satisfaction_scores = df.select("SatisfactionScore").toPandas()
    plt.figure(figsize=(10, 6))
    plt.hist(
        satisfaction_scores["SatisfactionScore"],
        bins=10,
        color="coral",
        edgecolor="black",
    )
    plt.xlabel("Satisfaction Score")
    plt.ylabel("Frequency")
    plt.title("Distribution of Satisfaction Scores")
    image_path = os.path.join(PLOT_DIR, "satisfaction_distribution.png")
    plt.savefig(image_path)  # Save figure
    plt.close()
    log_output(
        "Plot Satisfaction Distribution",
        "Distribution plot saved for Satisfaction Scores.",
        image_path,
    )


def end_spark(session: SparkSession):
    """Stop the Spark session."""
    session.stop()
    log_output("End Spark Session", "Spark session stopped.")
