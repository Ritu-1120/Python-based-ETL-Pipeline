import boto3
import pandas as pd
from io import StringIO
from config.aws_config import AWS_ACCESS_KEY, AWS_SECRET_KEY, S3_BUCKET_NAME, S3_FOLDER

def upload_to_s3(dataframe, filename):
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    
    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )
    
    s3_resource.Object(S3_BUCKET_NAME, f'{S3_FOLDER}/{filename}').put(Body=csv_buffer.getvalue())

if __name__ == "__main__":
    df = pd.DataFrame({'some_column': [1, 2, 3]})
    upload_to_s3(df, 'transformed_data.csv')
