import os

import pandas as pd

# Extraction
df = pd.read_csv('05-data-engineering-fundamentals/hands-on/data/Absenteeism_at_work.csv', sep=';')

# Transformation
def rename_columns(x):
    if " " in x:
        return x.replace(' ', '_').lower() 
    return x.lower()

# Load
df = df.rename(columns=rename_columns)
df.to_csv("05-data-engineering-fundamentals/hands-on/data/Absenteeism_at_work_transformed.csv", encoding='utf-8')

def run_etl():
    pass

if __name__ == "__main__":
    print(os.getcwd())
    run_etl()