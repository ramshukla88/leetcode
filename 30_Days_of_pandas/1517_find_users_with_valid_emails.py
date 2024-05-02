# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    email_split = users["mail"].str.split("@", n=1, expand=True)
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*$'
    valid_emails = users[email_split[0].str.match(pattern, na=False) & (email_split[1] == "leetcode.com")]
    return valid_emails[["user_id", "name", "mail"]]