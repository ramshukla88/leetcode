# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diab = patients[patients["conditions"].str.contains(r'\bDIAB1')]
    return diab[["patient_id", "patient_name","conditions"]]