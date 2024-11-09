"""
ETL-Query script
"""

import argparse
import sys
from mylib.query import general_query, read_data
from mylib.loading import load


# Handle arguments function
def handle_arguments(args):
    """Handles actions based on initial calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")

    # Define the action argument
    parser.add_argument(
        "action",
        choices=[
            "load",
            "general_query",
            "read_data",
        ],
    )
    # Parse only the action first
    args = parser.parse_args(args[:1])
    print(f"Action: {args.action}")

    # Define specific arguments for each action
    if args.action == "load":
        parser.add_argument(
            "--dataset", default="data/customer_feedback_satisfaction.csv"
        )

    if args.action == "general_query":
        parser.add_argument("query")

    # Parse again to get all the necessary arguments
    full_args = parser.parse_args(sys.argv[1:])
    return full_args


def main():
    args = handle_arguments(sys.argv[1:])

    if args.action == "load":
        load(args.dataset)
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)


if __name__ == "__main__":
    main()
