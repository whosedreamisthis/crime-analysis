import pandas as pd
import numpy as np
from .utils import clean_property_loss_usd_val,clean_crime_type,clean_incident_datetime

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    print("DEBUG: Entered function", flush=True)
    df = pd.read_csv(filepath)
    initial_count = len(df)
    
    df.property_loss_usd = df.property_loss_usd.apply(clean_property_loss_usd_val)
    df = df.dropna(subset=["property_loss_usd"])
    dropped_count = initial_count - len(df)
    print(f"Cleaned property loss. Dropped {dropped_count} rows with unrecoverable targets.", flush=True)
    df.property_loss_usd = df.property_loss_usd.apply(lambda x: max(0.0, x))

    df.crime_type = df.crime_type.apply(clean_crime_type)
    print(f"Cleaned crime_type. Missing: {df.crime_type.isna().sum()}")

    df['incident_datetime'] = df['incident_datetime'].apply(clean_incident_datetime)
    
    
    df['incident_datetime_missing'] = df['incident_datetime'].isna().astype(int)
    print("Created incident_datetime missing indicator", flush=True)

    # Check nulls BEFORE filling so it prints a meaningful number (> 0)
    
    

    df['incident_datetime'] = df['incident_datetime'].fillna(pd.Timestamp('1970-01-01'))
    print(f"cleaned incident_datetime. type: {df.incident_datetime.dtype} Missing: {df.incident_datetime.isna().sum()}")
   
    
    return df
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    initial_count = len(df)
    df.property_loss_usd = df.property_loss_usd.apply(clean_property_loss_usd_val)
    df = df.dropna(subset=["property_loss_usd"])
    dropped_count = initial_count - len(df)
    print(f"Cleaned property loss. Dropped {dropped_count} rows with unrecoverable targets.")
    df.property_loss_usd = df.property_loss_usd.apply(lambda x: max(0.0,x))
    try:
        df.crime_type = df.crime_type.apply(clean_crime_type)

        df['incident_datetime'] = df['incident_datetime'].apply(clean_incident_datetime)
    
        df['incident_datetime_missing'] = df['incident_datetime'].isna().astype(int)

        df['incident_datetime'] = df['incident_datetime'].fillna(pd.Timestamp('1970-01-01'))
        null_itd = df.incident_datetime.isna().sum()
        print(f"incident_datetime number of null entries: {null_itd}",flush=True)
    except Exception as e:
        print(f"CRASHED: {type(e).__name__}: {e}")
    return df
    