"""
ETL-Query script
"""

import argparse
import sys
from mylib.query import general_query, create_rec, update_rec, delete_rec, read_data
from mylib.transform_load import load


# Handle arguments function
def handle_arguments(args):
    """Handles actions based on initial calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")

    # Define the action argument
    parser.add_argument(
        "action",
        choices=[
            "load",
            "create_rec",
            "update_rec",
            "delete_rec",
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

    if args.action == "create_rec":
        parser.add_argument("customer_id", type=int)
        parser.add_argument("age", type=int)
        parser.add_argument("gender")
        parser.add_argument("country")
        parser.add_argument("income", type=float)
        parser.add_argument("product_quality", type=int)
        parser.add_argument("service_quality", type=int)
        parser.add_argument("purchase_frequency", type=int)
        parser.add_argument("feedback_score", type=int)
        parser.add_argument("loyalty_level")
        parser.add_argument("satisfaction_score", type=float)

    if args.action == "update_rec":
        parser.add_argument("customer_id", type=int)
        parser.add_argument("age", type=int)
        parser.add_argument("gender")
        parser.add_argument("country")
        parser.add_argument("income", type=float)
        parser.add_argument("product_quality", type=int)
        parser.add_argument("service_quality", type=int)
        parser.add_argument("purchase_frequency", type=int)
        parser.add_argument("feedback_score", type=int)
        parser.add_argument("loyalty_level")
        parser.add_argument("satisfaction_score", type=float)

    if args.action == "delete_rec":
        parser.add_argument("customer_id", type=int)

    if args.action == "general_query":
        parser.add_argument("query")

    # Parse again to get all the necessary arguments
    full_args = parser.parse_args(sys.argv[1:])
    return full_args


def main():
    args = handle_arguments(sys.argv[1:])

    if args.action == "load":
        load(args.dataset)
    elif args.action == "create_rec":
        create_rec(
            args.customer_id,
            args.age,
            args.gender,
            args.country,
            args.income,
            args.product_quality,
            args.service_quality,
            args.purchase_frequency,
            args.feedback_score,
            args.loyalty_level,
            args.satisfaction_score,
        )
    elif args.action == "update_rec":
        update_rec(
            args.customer_id,
            args.age,
            args.gender,
            args.country,
            args.income,
            args.product_quality,
            args.service_quality,
            args.purchase_frequency,
            args.feedback_score,
            args.loyalty_level,
            args.satisfaction_score,
        )
    elif args.action == "delete_rec":
        delete_rec(args.customer_id)
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)


if __name__ == "__main__":
    main()
