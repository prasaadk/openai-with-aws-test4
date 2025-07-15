import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = os.environ['BUCKET_NAME']
    key = 'lambda_output.txt'
    content = 'file created by lambda'
    s3.put_object(Bucket=bucket, Key=key, Body=content)
    return {
        'statusCode': 200,
        'body': f'File {key} created in {bucket}'
    }

