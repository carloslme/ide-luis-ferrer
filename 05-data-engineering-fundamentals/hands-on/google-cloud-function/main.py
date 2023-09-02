import os
from google.cloud import storage
import pandas as pd


# Initialize the Cloud Storage client.
storage_client = storage.Client()

# Extraction
def extract_data(path: str):

    fileName = "gs://itesm-mlops-test/Absenteeism_at_work_01_09_2023.csv"

    df = pd.read_csv(fileName, sep=",")
    print(df)
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
def load_data(df: pd.DataFrame):
    # The bucket on GCS in which to write the CSV file
    bucket = storage_client.bucket('itesm-mlops-test-load')
    # The name assigned to the CSV file on GCS
    blob = bucket.blob('Absenteeism_at_work_01_09_2023_Transformed.csv')
    blob.upload_from_string(df.to_csv(), 'text/csv')
    print("Data Loaded")
    return "Ok"

def run_etl(request):
    raw_data_path = '05-data-engineering-fundamentals/hands-on/data/Absenteeism_at_work.csv'
    
    raw_df = extract_data(raw_data_path)
    transformed_df = transform_data(raw_df)
    result = load_data(transformed_df)
    if result is "Ok":
        return 'Dataframe saved in itesm-mlops-test-load/Absenteeism_at_work_01_09_2023_Transformed.csv'
    else:
        return "Not Ok"


