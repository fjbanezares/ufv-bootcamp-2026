import boto3
from botocore.exceptions import NoCredentialsError

try:
    s3 = boto3.client('s3')
    # Check if the credentials are valid by listing buckets
    response = s3.list_buckets()
    print("Credentials are valid. Here's a list of your S3 buckets:")
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
except NoCredentialsError:
    print("No valid credentials found.")
