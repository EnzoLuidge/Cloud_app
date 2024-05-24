# Cloud Application with AWS Auto Scaling and DynamoDB

stackzada-MyALB-1510882621.sa-east-1.elb.amazonaws.com loadbalancer link for example

This project demonstrates how to deploy a scalable web application using AWS services, including EC2, Auto Scaling, Application Load Balancer (ALB), and DynamoDB. The application is a simple Flask web app that allows users to create, read, update, and delete posts, with data stored in DynamoDB.

# Table of Contents

Architecture

Prerequisites

Setup

Deploying the CloudFormation Stack

Setting Up the CI/CD Pipeline

Using the Application

Load Testing with Locust

Cleanup

# Architecture

The architecture of this project includes the following components:

VPC: A Virtual Private Cloud to host the resources.

Subnets: Two public subnets in different availability zones.

Internet Gateway: To allow internet access.

Security Groups: To control inbound and outbound traffic.

EC2 Instances: Hosting the Flask application.

Auto Scaling Group: To automatically scale the number of EC2 instances based on demand.

Application Load Balancer (ALB): To distribute incoming traffic across multiple EC2 instances.

DynamoDB: To store application data.

IAM Roles: To provide the necessary permissions to EC2 instances.

CodePipeline: For continuous integration and deployment (CI/CD).

Secrets Manager: For securely storing and accessing secrets such as GitHub tokens.

# Prerequisites

Before you begin, ensure you have the following:

An AWS account with appropriate permissions to create resources.

AWS CLI installed and configured.

An SSH key pair in your AWS account (you'll need the key pair name).

A GitHub account and repository forked from Cloud_app.

# Setup
Clone the repository:

git clone https://github.com/EnzoLuidge/Cloud_app.git

cd Cloud_app

Update the CloudFormation Template:

Ensure the template.yaml file located in the YAML directory has the correct AMI ID for your region and the name of your SSH key pair:

Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-04716897be83e3f04 # Update this to a valid AMI ID in your region
      KeyName: YourKeyPairName # Update this to your key pair name
      
Install Python dependencies:

pip install -r requirements.txt

Deploying the CloudFormation Stack

Navigate to the YAML directory:

cd YAML

Create the CloudFormation stack for the infrastructure:

aws cloudformation create-stack --stack-name stackzada --template-body file://template.yaml --capabilities CAPABILITY_IAM

Wait for the stack to be created:

You can monitor the stack creation process in the AWS CloudFormation console.

# Setting Up the CI/CD Pipeline

Once the infrastructure stack is created, you need to set up the CI/CD pipeline:

Create a secret in AWS Secrets Manager to store your GitHub token:

Go to the AWS Secrets Manager console.

Click "Store a new secret".

Choose "Other type of secrets".

Add a secret key github_token and your GitHub token as the value.

Name the secret MyGithubToken.

Create the CloudFormation stack for the pipeline:

aws cloudformation create-stack --stack-name MyPipelineStack --template-body file://pipeline.yaml --capabilities CAPABILITY_NAMED_IAM

This stack sets up a CodePipeline that automatically deploys updates to your application when changes are pushed to your GitHub repository.

# Using the Application

Once the stack is created, follow these steps to use the application:

Retrieve the Load Balancer DNS Name:

Go to the AWS Management Console.

Navigate to the EC2 Dashboard.

Click on "Load Balancers" in the left menu.

Find the ALB created by the CloudFormation stack and copy its DNS name.

# Access the Application:

Open your web browser and navigate to the ALB DNS name. You should see the application homepage where you can add, view, edit, and delete posts.

# Load Testing with Locust
To perform load testing on the application, follow these steps:

Install Locust:

pip install locust

Navigate to the LOCUST directory:

cd LOCUST

Run Locust:

locust -f locust.py

Open Locust Web Interface:

Open your web browser and navigate to http://localhost:8089. Configure the number of users and the spawn rate. Start the test to simulate load on your application.

Cleanup

To delete all resources created by the CloudFormation stack, run:

aws cloudformation delete-stack --stack-name stackzada

aws cloudformation delete-stack --stack-name MyPipelineStack

This will clean up all the resources created by the CloudFormation stacks, including the infrastructure and the CI/CD pipeline.
