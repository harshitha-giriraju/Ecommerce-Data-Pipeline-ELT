from typing import Dict
from pandas import DataFrame
import sqlite3
from src.config import SQLITE_BD_ABSOLUTE_PATH


# Explicit correct mapping
EXTRACT_TO_FINAL = {
    "customers": "olist_customers",
    "orders": "olist_orders",
    "order_items": "olist_order_items",
    "payments": "olist_order_payments",
    "reviews": "olist_order_reviews",
    "products": "olist_products",
    "sellers": "olist_sellers",
    "geolocation": "olist_geolocation",
    "translations": "product_category_name_translation",
    "public_holidays": "public_holidays"  # Or whatever name transform.py expects
}


def load(data_frames: Dict[str, DataFrame]):

    with sqlite3.connect(SQLITE_BD_ABSOLUTE_PATH) as conn:
        for extracted_name, df in data_frames.items():

            if extracted_name not in EXTRACT_TO_FINAL:
                print(f"⚠️ WARNING: No mapping for {extracted_name}, skipping.")
                continue

            final_name = EXTRACT_TO_FINAL[extracted_name]

            df.to_sql(final_name, conn, if_exists="replace", index=False)
            print(f"✔ Loaded {extracted_name} → {final_name}")

    print("\nLoaded into:", SQLITE_BD_ABSOLUTE_PATH)


if __name__ == "__main__":
    from src.extract import extract
    dfs = extract()
    load(dfs)
