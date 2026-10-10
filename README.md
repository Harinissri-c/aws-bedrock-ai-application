# AI Application using AWS Bedrock

## 📌 Overview
This project is a serverless AI application built using AWS services. It processes user queries and generates intelligent, context-aware responses using Amazon Bedrock and Knowledge Bases.

---

## 🏗️ Architecture
User → API Gateway → AWS Lambda → AWS Bedrock → Response

---

## 🧰 AWS Services Used
- API Gateway  
- AWS Lambda (Python)  
- Amazon Bedrock  
- Bedrock Knowledge Base  
- Amazon S3  
- IAM  
- CloudWatch  

---

## ⚙️ Features
- AI-powered response generation  
- RAG using Bedrock Knowledge Base  
- Serverless architecture  
- Secure IAM-based access  

---

## 🔄 Workflow
1. User sends request via API Gateway  
2. Lambda processes input  
3. Query sent to Bedrock Knowledge Base  
4. Data retrieved from S3  
5. Response generated and returned  

---

## 🚀 API Endpoint

POST  
https://your-api-id.execute-api.region.amazonaws.com/prod/

---

## 🧪 Testing with Postman

### Headers:
Content-Type: application/json

### Body:
{
  "question": "What is AWS Bedrock?"
}

---

## ⚙️ Setup
- Create Lambda function  
- Configure IAM roles  
- Setup API Gateway  
- Connect Knowledge Base with S3  
- Deploy and test  

---

## 👤 Author
Harini ssri C
