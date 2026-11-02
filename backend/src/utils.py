import re
import pandas as pd
import numpy as np

def clean_crime_type(val):
    if pd.isna(val):
        return "Unknown"
    
    # 1. Normalize spacing and title case
    text = str(val).strip()
    text = re.sub(r'\s+', ' ', text)  # Collapse double/triple spaces
    text = text.title()
    
    # 2. Standardization mapping dictionary for typos, abbreviations, and synonyms
    mapping = {
        # Arson
        "Arsen": "Arson",
        "Fire Setting": "Arson",
        
        # Assault & Battery variants
        "Asslt": "Assault",
        "Assault  &  Battery": "Assault & Battery",
        
        # Breaking & Entering / Burglary
        "B&E": "Breaking & Entering",
        "Burglry": "Burglary",
        
        # Cyber Crime / Online Fraud / Hacking
        "Cybercrime": "Cyber Crime",
        "Hacking": "Cyber Crime",
        "Online Fraud": "Cyber Crime",
        
        # Domestic Violence
        "Dv": "Domestic Violence",
        "Dom. Violence": "Domestic Violence",
        "Domestc Violence": "Domestic Violence",
        "Domestic  Violence": "Domestic Violence",
        
        # Drug Offense / Narcotics
        "Drug  Offence": "Drug Offense",
        "Drug  Offense": "Drug Offense", # (or Drug Offence)
        "Drug Offence": "Drug Offense",
        "Drugs": "Drug Offense",
        "Narcotics": "Drug Offense",
        
        # DUI / Drunk Driving / DWI
        "D.U.I.": "Dui",
        "Duii": "Dui",
        "Drunk Driving": "Dui",
        "Dwi": "Dui",
        
        # Fraud / Scam / Deception
        "Fraudulent Activity": "Fraud",
        
        # Homicide / Murder / Manslaughter
        "Homocide": "Homicide",
        
        # Kidnapping
        "Kidnaping": "Kidnapping",
        
        # Property Damage / Vandalism / Graffiti
        "Graffiti": "Vandalism",
        "Vandlism": "Vandalism",
        
        # Robbery
        "Robbry": "Robbery",
        "Roberry": "Robbery",
        "Armed  Robbery": "Armed Robbery",
        
        # Sexual Assault
        "Sa": "Sexual Assault",
        "Sex Assault": "Sexual Assault",
        "Sex  Assault": "Sexual Assault",
        "Sexual  Assault": "Sexual Assault",
        "Sexual  Assualt": "Sexual Assault",
        "Sexual Assualt": "Sexual Assault",
        
        # Theft / Larceny / Stealing
        "Stealing": "Theft",
        "Larceny": "Theft",
        "Theft/Larceny": "Theft",
        
        # Trespassing
        "Trespass": "Trespassing",
        "Tresspassing": "Trespassing"
    }
    
    return mapping.get(text, text)

def clean_property_loss_usd_val(val):
    if pd.isna(val):
        return np.nan
    val_str = str(val).strip()

    if val_str.endswith(".0") and val_str[:-2].count('.') >= 1:
        val_str = val_str[:-2]

    try:
        return float(val_str)
    except ValueError:
        return np.nan
    

def clean_incident_datetime(val):
    """
    Cleans and standardizes a single incident datetime string/value.
    Returns a pandas Timestamp object or None if invalid/missing.
    """
    if pd.isna(val) or str(val).strip() == "":
        return None
    
    # Attempt parsing using pandas to_datetime with mixed format support
    parsed = pd.to_datetime(val, format='mixed', errors='coerce')
    
    if pd.isna(parsed):
        return None
        
    return parsed
