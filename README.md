AWS Weather Monitoring System

This project implements a real-time weather monitoring and alert system based on geographic coordinates (latitude and longitude). Weather data is collected from the Tomorrow.io API and processed using AWS services. The system performs continuous monitoring and generates alerts when specific weather conditions are detected.

The data collection process is handled by an AWS Lambda function executed on a scheduled basis. This function consumes real weather data from the Tomorrow.io API using a predefined latitude and longitude as input and sends the collected information to an Amazon Kinesis Data Stream.

Amazon Kinesis acts as an event broker, enabling real-time streaming and processing of the weather data. A consumer Lambda function processes the incoming stream in near real time, analyzes weather conditions and publishes alert events to an Amazon SNS topic whenever predefined thresholds are met.

Amazon SNS is responsible for delivering weather alerts automatically to the user via email and SMS using the contacts registered in the AWS environment. These notifications are triggered based on the analysis performed during the real-time processing stage.

In parallel, a batch consumer Lambda function processes the same data stream and stores the weather data in an Amazon S3 bucket, creating a historical dataset. This stored data is cataloged using an AWS Glue Crawler, allowing structured access through the AWS Glue Data Catalog.

Once cataloged, the data can be queried using Amazon Athena, enabling SQL-based analysis and validation of the collected meteorological information.

Security and access control are managed using AWS IAM, ensuring that each service and function operates with the minimum required permissions.

This project was developed as part of a hands-on AWS course with the goal of consolidating practical knowledge in cloud architecture, event-driven systems, automation, streaming data and external API integration. All AWS resources were provisioned, tested and later deactivated to avoid recurring costs. The repository contains the full source code and real screenshots of the AWS environment during the execution of the project.
