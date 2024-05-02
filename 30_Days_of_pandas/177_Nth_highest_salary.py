# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary'])
    sorted_salaries = sorted(employee["salary"], reverse=True)
    
    # Check if N is within the valid range
    if N <= 0 or N > len(sorted_salaries):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    nth_highest = sorted_salaries[N - 1] if N <= len(sorted_salaries) else None
    
    # If nth_highest is None, it means there are fewer salaries than N, return an empty DataFrame
    if nth_highest is None:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    
    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest]})