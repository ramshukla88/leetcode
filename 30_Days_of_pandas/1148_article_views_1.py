# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]]
    df = df.drop_duplicates(subset="author_id") #drop duplicates
    df.rename(columns={"author_id":"id"}, inplace=True) #rename the author_id column to id
    df.sort_values(by=["id"], inplace=True) #sort the output
    # All three operations can pe done in one line also: This has good space complexity
    """
    df = views[views["author_id"] == views["viewer_id"]] \
        .drop_duplicates(subset="author_id") \
        .rename(columns={"author_id":"id"}) \
        .sort_values(by="id")"""
    return df[["id"]]