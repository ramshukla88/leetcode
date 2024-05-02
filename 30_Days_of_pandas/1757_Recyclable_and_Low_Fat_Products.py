# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products["low_fats"]=="Y") & (products["recyclable"]== "Y")]
    return df[["product_id"]]