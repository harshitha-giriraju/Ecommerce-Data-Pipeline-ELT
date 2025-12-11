from typing import Dict
import requests
from pandas import DataFrame, read_csv, to_datetime


def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    response = requests.get(f"{public_holidays_url}/{year}/BR")
    response.raise_for_status()
    holidays = response.json()
    holidays_df = DataFrame(holidays)
    holidays_df = holidays_df.drop(columns=["types", "counties"], errors="ignore")
    holidays_df["date"] = to_datetime(holidays_df["date"])
    return holidays_df


def extract(
    csv_folder: str = "dataset",
    csv_table_mapping: Dict[str, str] = None,
    public_holidays_url: str = "https://date.nager.at/api/v3/PublicHolidays"
) -> Dict[str, DataFrame]:

    if csv_table_mapping is None:
        csv_table_mapping = {
            "olist_customers_dataset.csv": "customers",
            "olist_orders_dataset.csv": "orders",
            "olist_order_items_dataset.csv": "order_items",
            "olist_order_payments_dataset.csv": "payments",
            "olist_order_reviews_dataset.csv": "reviews",
            "olist_products_dataset.csv": "products",
            "olist_sellers_dataset.csv": "sellers",
            "olist_geolocation_dataset.csv": "geolocation",
            "product_category_name_translation.csv": "translations",
        }

    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    holidays = get_public_holidays(public_holidays_url, "2017")
    dataframes["public_holidays"] = holidays
    return dataframes


# Allow running directly: python src/extract.py
if __name__ == "__main__":
    dfs = extract()
    print("Extracted tables:", list(dfs.keys()))
