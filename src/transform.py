import os
from enum import Enum
from sqlalchemy import create_engine
from src.config import SQLITE_BD_ABSOLUTE_PATH
from pandas import read_sql_query


from pathlib import Path

QUERIES_ROOT_PATH = Path(__file__).parent.parent / "queries"


class QueryNames(Enum):
    REVENUE_BY_MONTH_YEAR = "revenue_by_month_year"
    REVENUE_PER_STATE = "revenue_per_state"
    DELIVERY_DATE_DIFFERENCE = "delivery_date_difference"
    GLOBAL_AMOUNT_ORDER_STATUS = "global_ammount_order_status"
    ORDERS_PER_DAY_HOLIDAYS = "orders_per_day_and_holidays_2017"
    TOP_10_REVENUE_CATEGORIES = "top_10_revenue_categories"
    TOP_10_SELLERS_REVENUE = "top_10_sellers_by_revenue"


def get_query_content(query_name: str) -> str:
    file_path = QUERIES_ROOT_PATH / f"{query_name}.sql"

    if not file_path.exists():
        raise FileNotFoundError(f"SQL file missing: {file_path}")

    with open(file_path, "r") as file:
        return file.read()



def run_queries(engine=None):

    if engine is None:
        engine = create_engine(f"sqlite:///{SQLITE_BD_ABSOLUTE_PATH}")

    results = {}

    for query in QueryNames:
        sql = get_query_content(query.value)
        results[query.value] = read_sql_query(sql, engine)

    return results


# Run manually: python src/transform.py
if __name__ == "__main__":
    engine = create_engine(f"sqlite:///{SQLITE_BD_ABSOLUTE_PATH}")
    results = run_queries(engine)
    print("Executed queries:", list(results.keys()))
