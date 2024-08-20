import snowflake.connector
from config.snowflake_config import (
    SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, 
    SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA, SNOWFLAKE_TABLE
)

def load_to_snowflake(file_path):
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    
    cursor = conn.cursor()
    sql = f"""
    COPY INTO {SNOWFLAKE_TABLE}
    FROM '{file_path}'
    FILE_FORMAT = (TYPE = 'CSV', FIELD_OPTIONALLY_ENCLOSED_BY = '"')
    """
    cursor.execute(sql)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    s3_file_path = f"s3://{S3_BUCKET_NAME}/{S3_FOLDER}/transformed_data.csv"
    load_to_snowflake(s3_file_path)
