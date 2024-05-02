# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world["population"] >=  25000000) | (world["area"] >= 3000000)] # filter columns based on given crieteria
    return df[["name", "population", "area"]]  #return the required columns only