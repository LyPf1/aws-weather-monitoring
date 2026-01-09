import json
import requests
import boto3
import os

#API config
latitude = -29.6846 
longitude = -51.1419 
TOMORROW_API_KEY = os.getenv('TOMORROW_API_KEY')
url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={TOMORROW_API_KEY}"
headers = {"accept": "application/json"}

#Kinesis config
STREAM_NAME = "broker"
REGION = "us-east-1"

#customer config
kinesis_client = boto3.client('kinesis', region_name=REGION)

def lambda_handler(event, context):
    #api request
    response = requests.get(url, headers=headers)
    weather_data = response.json()

    #send data to Kinesis
    kinesis_client.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(weather_data),
        PartitionKey="partition_key"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados enviados ao Kinesis com sucesso')
    }

