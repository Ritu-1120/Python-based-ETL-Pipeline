from extract.api_data_extractor import fetch_data
from transform.data_transformer import transform_data
from load.s3_uploader import upload_to_s3
from load.snowflake_loader import load_to_snowflake

def main():
    # Step 1: Extract
    api_url = 'https://api.example.com/data'
    raw_data = fetch_data(api_url)
    
    # Step 2: Transform
    transformed_data = transform_data(raw_data)
    
    # Step 3: Load to S3
    upload_to_s3(transformed_data, 'transformed_data.csv')
    
    # Step 4: Load to Snowflake
    s3_file_path = 's3://your_s3_bucket_name/your_s3_folder/transformed_data.csv'
    load_to_snowflake(s3_file_path)

if __name__ == "__main__":
    main()
