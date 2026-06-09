import os
import pandas as pd
from functools import partial

ENDPOINT = "https://minio.terrafoxai.com"

def connect(user=None, password=None):
    user = user or os.environ.get("MINIO_USER")
    password = password or os.environ.get("MINIO_PASSWORD")
    
    if not user or not password:
        import getpass
        print("🔐 Data Lake credentials not found in environment settings.")
        user = user or input("Enter MinIO Username: ")
        password = password or getpass.getpass("Enter MinIO Password: ")

    os.environ["AWS_ACCESS_KEY_ID"] = user
    os.environ["AWS_SECRET_ACCESS_KEY"] = password
    
    pd.read_csv = partial(pd.read_csv, storage_options={
        "key": user, 
        "secret": password, 
        "client_kwargs": {"endpoint_url": ENDPOINT}
    })
    
    print("🚀 Terrafox Data Lake Connected Natively via Background Environment!")

def get_spark(app_name="Terrafox-DataLake"):
    from pyspark.sql import SparkSession
    user = os.environ.get("AWS_ACCESS_KEY_ID")
    password = os.environ.get("AWS_SECRET_ACCESS_KEY")
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.hadoop.fs.s3a.endpoint", ENDPOINT) \
        .config("spark.hadoop.fs.s3a.access.key", user) \
        .config("spark.hadoop.fs.s3a.secret.key", password) \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()
