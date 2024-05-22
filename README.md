# Cloud Application with AWS Auto Scaling and DynamoDB

This project demonstrates how to deploy a scalable web application using AWS services, including EC2, Auto Scaling, Application Load Balancer (ALB), and DynamoDB. The application is a simple Flask web app that allows users to create, read, update, and delete posts, with data stored in DynamoDB.

## Table of Contents

Architecture

Prerequisites

Setup

Deploying the CloudFormation Stack

Using the Application

Cleanup


## Architecture

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


## Prerequisites

Before you begin, ensure you have the following:

An AWS account with appropriate permissions to create resources.
AWS CLI installed and configured.
An SSH key pair in your AWS account (you'll need the key pair name).

## Setup

Clone the repository:

git clone https://github.com/EnzoLuidge/Cloud_app.git
cd Cloud_app
Update the CloudFormation Template:
Ensure the template.yaml file has the correct AMI ID for your region and the name of your SSH key pair:


MyEC2Instance:
  Properties:
    ImageId: ami-04716897be83e3f04 # Update this to a valid AMI ID in your region
    KeyName: YourKeyPairName # Update this to your key pair name

## Deploying the CloudFormation Stack

Create the CloudFormation stack:

aws cloudformation create-stack --stack-name MyCloudAppStack --template-body file://template.yaml --capabilities CAPABILITY_IAM
Wait for the stack to be created:
You can monitor the stack creation process in the AWS CloudFormation console.

## Using the Application

Once the stack is created, follow these steps to use the application:

Retrieve the Load Balancer DNS Name:

Go to the AWS Management Console.
Navigate to the EC2 Dashboard.
Click on "Load Balancers" in the left menu.
Find the ALB created by the CloudFormation stack and copy its DNS name.
Access the Application:

Open your web browser and navigate to the ALB DNS name.
You should see the application homepage where you can add, view, edit, and delete posts.

## Cleanup

To delete all resources created by the CloudFormation stack, run:

aws cloudformation delete-stack --stack-name MyCloudAppStack
