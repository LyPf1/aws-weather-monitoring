import json
import boto3
import base64
import os
from datetime import datetime

#s3 client
s3_client = boto3.client('s3')

BUCKET_NAME = os.getenv('BUCKET_NAME')

def lambda_handler(event, context):
    for record in event['Records']:
        #decode kinesis registry
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        #get date
        now = datetime.utcnow()
        year = now.year
        month = now.month
        day = now.day

        #create unique folder with date partitions
        file_name = f"raw/year={year}/month={month}/day={day}/weather_data_{now.isoformat()}.json"
        
        #save data in bucket s3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos no S3 com sucesso')
    }

