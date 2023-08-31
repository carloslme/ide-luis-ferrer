import os

import pandas as pd

# Extraction
def extract_data(path: str):
    df = pd.read_csv(path, sep=';')
    print("Data Extracted")
    return df

# Transformation
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """This function transform the input data.

    Args:
        df (pd.DataFrame): Raw dataframe
    Returns:
        pd.DataFrame: Transformed dataframe
    """
    def rename_columns(x):
        if " " in x:
            return x.replace(' ', '_').replace('/', '_').lower() 
        return x.lower()
    df = df.rename(columns=rename_columns)
    print("Data Transformed")
    return df

# Load
def load_data(path: str, df: pd.DataFrame):
    df.to_csv(path, encoding='utf-8')
    print("Data Loaded")

def run_etl(raw_data_path: str, output_data_pat: str):
    raw_df = extract_data(raw_data_path)
    transformed_df = transform_data(raw_df)
    load_data(output_data_pat, transformed_df)
    

if __name__ == "__main__":
    print(os.getcwd())
    raw_data_path = '05-data-engineering-fundamentals/hands-on/data/Absenteeism_at_work.csv'
    output_data_path = "05-data-engineering-fundamentals/hands-on/data/staging/Absenteeism_at_work_transformed.csv"
    run_etl(raw_data_path, output_data_path)