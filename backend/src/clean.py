import pandas as pd
import numpy as np
from .utils import clean_property_loss_usd_val

def load_and_clean_data(filepath:str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    initial_count = len(df)
    df.property_loss_usd = df.property_loss_usd.apply(clean_property_loss_usd_val)
    df = df.dropna(subset=["property_loss_usd"])
    dropped_count = initial_count - len(df)
    print(f"Cleaned property loss. Dropped {dropped_count} rows with unrecoverable targets.")
    df.property_loss_usd = df.property_loss_usd.apply(lambda x: max(0.0,x))
    
    return df
    