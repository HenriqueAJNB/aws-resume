# 📚 Projects documentation

## 🏗️ Architecture

![architecture](.//img/architecture.png)

### 🔧 Components

- **Frontend**: Static HTML/CSS/JavaScript website hosted on Amazon S3.
- **Backend**: Serverless architecture using AWS Lambda, API Gateway, and DynamoDB.
- **Infrastructure**: AWS Cloud infrastructure managed manually.

## 🖥️ Frontend documentation

### 📂 Website structure

- `index.html`: Main HTML resume page.
- `style.css`: Contains CSS formating applied to HTML.
- `visitors_counter.js`: Contains the visitor counter JavaScript implementation calling backend services.

### 🔢 Visitors counter

The visitors counter were implemented in pure JavaScript and can be found here. It basically invokes the API Gateway and receive it's response and update it into HTML element to be displayed on webpage. Each webpage hit increments one at the visitors counter.

⚠️ It is important to highlight that it's simply count each hit on webpage, and not the number of unique visitors (by capturing IP address or coockies for example).

## ⚙️ Backend documentation

### ☁️ AWS components setup

#### 🪣 S3 configuration

- AWS S3 Bucket to store content.
- Static website hosting enabled.
- Public access configured.

#### 🌐 API Gateway

- REST API endpoint for counter functionality
- Integrated with Lambda function.

#### 📰 Lambda Function

The Lambda Function implements the reading and updating visitors counter information stored in DynamoDB. It adds one to a record each time the funcion is invoked. The implementation was provided in Python language and can be found at this file.

#### 📊 DynamoDB

The DynamoDB store the number of visitors at resume website. A record is read and updated by one unit trought Lambda Funtion each time that someone clicks on page.

### 🔐 IAM roles and permissions

- Lambda execution role with DynamoDB access.
- API Gateway permissions to invoke Lambda.
- S3 bucket policy for public read access.
- CORS enabled for S3 website domain for security purposes.

## 🤑 Cost analysis

WIP
