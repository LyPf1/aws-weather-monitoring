# AWS Weather Monitoring System

Simple cloud-based project developed for academic and hands-on purposes,  
demonstrating event-driven architecture, API integration, automation, and AWS cost-aware usage.

## Technologies
- AWS Lambda  
- Amazon Kinesis Data Streams  
- Amazon S3  
- Amazon SNS (Email and SMS notifications)  
- AWS IAM  
- AWS Glue  
- Amazon Athena  
- Amazon CloudWatch  
- Python  
- Tomorrow.io API  

## Project Workflow (Step by Step)
1. **Weather data collection**  
   - An AWS Lambda function (producer) runs automatically based on a schedule configured with CloudWatch.  
   - This function consumes real weather data from the Tomorrow.io API, using a predefined latitude and longitude as input.  

2. **Streaming data ingestion**  
   - The collected data is sent to an Amazon Kinesis Data Stream, which acts as an event broker, enabling continuous data processing.  

3. **Real-time processing and alerts**  
   - A second AWS Lambda function (consumer_realtime) consumes data directly from the Kinesis stream.  
   - This function analyzes weather conditions and, when predefined alert conditions are met, publishes a message to an Amazon SNS topic.  
   - SNS sends automatic alerts via email and SMS to the contacts registered in the AWS environment.  

4. **Batch processing and data storage**  
   - In parallel with real-time processing, an AWS Lambda function (consumer_batch) processes the data for storage.  
   - Weather data is stored in an Amazon S3 bucket, creating a historical dataset for future analysis.  

5. **Data cataloging and analysis**  
   - An AWS Glue Crawler catalogs the data stored in S3 into the Glue Data Catalog.  
   - Once cataloged, the data can be queried using Amazon Athena, allowing SQL-based analysis and validation of the collected data.  

6. **Security and access control**  
   - The project uses AWS IAM to manage permissions, ensuring that each service and function has access only to the required resources, following the principle of least privilege.  

## User Notifications
The system sends real weather alerts automatically:  
- 📧 Via email  
- 📱 Via SMS  

Notifications are triggered whenever specific weather conditions are detected during real-time data processing.  

## Important Notes
- This project was developed based on a hands-on AWS course, with the goal of consolidating knowledge in cloud architecture, automation, streaming data, and external API integration.  
- All AWS resources were provisioned, tested, and later deactivated to avoid recurring costs.  
- This repository contains the full source code, documentation, and real screenshots from the AWS environment during the project execution.  

## Evidence
The `aws-weather-monitoring/screenshots_proof/` directory contains real screenshots of the project in operation, including:  
- Amazon Athena queries and results  
- AWS Lambda executions  
- Active Kinesis Data Stream  
- S3 data structure  
- SNS notification configuration  
