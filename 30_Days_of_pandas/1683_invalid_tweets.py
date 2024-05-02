# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets["content"].str.len() > 15]
    return df[["tweet_id"]]