# 📚 Projects Documentation

## 🏗️ Architecture

![architecture](.//img/architecture.png)

The architecture illustrates a serverless web application divided into a static frontend and a serverless backend. The frontend is hosted on Amazon S3, distributed via CloudFront, and secured with SSL/TLS. The backend uses API Gateway and Lambda to handle dynamic requests, updating the visitor count in DynamoDB.

---

## 🔧 Components

- **Frontend**: Static HTML/CSS/JavaScript website hosted on Amazon S3, distributed through Amazon CloudFront and Amazon Route 53.
- **Backend**: Serverless architecture using AWS Lambda, API Gateway, and DynamoDB.
- **Infrastructure**: AWS Cloud infrastructure managed manually.

---

## 🖥️ Frontend documentation

### 📂 Website structure

- **`index.html`**: Main HTML page for the resume.
- **`style.css`**: Contains CSS formatting for the website.
- **`visitors_counter.js`**: Implements the visitor counter, calling backend services.

---

### 🛫 Routes structure

#### **Amazon Route 53**

- Routes traffic to the custom domain linked to the static website hosted on S3 and provides global DNS resolution.

#### **Amazon CloudFront**

- Distributes static files (HTML, CSS, JS) from S3 to edge locations for faster delivery.
- Caches content globally to minimize latency.
- Ensures secure connections using SSL/TLS certificates issued by Amazon Certificate Manager.

#### **Amazon Certificate Manager**

- Provides SSL/TLS certificates for encrypting user communications.
- Integrated with CloudFront for redirecting HTTP to HTTPS traffic.

#### **Amazon S3**

- Hosts static website files (HTML, CSS, JS) with public access enabled and configured for static website hosting, serving the content globally through CloudFront.

---

### 🔢 Visitors counter

The visitors counter is implemented in pure JavaScript (`visitors_counter.js`) and performs the following steps:

1. Calls the API Gateway to retrieve the current counter value.
2. Updates the counter value in DynamoDB via a Lambda function.
3. Displays the updated count dynamically on the webpage.

**⚠️ Important:**  
This counter increments for every page hit and does not track unique visitors (e.g., no IP or cookie-based filtering).

---

## ⚙️ Backend documentation

### ☁️ AWS components setup

#### 🪣 S3 configuration

- Stores static website files (HTML, CSS, JS).
- Static website hosting is enabled, with public read access configured.

#### 🌐 API Gateway

- Provides a REST API endpoint for the counter functionality.
- Integrates with Lambda to handle requests and responses.

#### 📰 Lambda Function

- Implements backend logic to read and update the visitor counter stored in DynamoDB.
- Written in Python, the function increments a record each time it is invoked.

#### 📊 DynamoDB

- Stores the visitor count as a single record.
- The counter is updated by the Lambda function for each API call.

---

### 🔐 IAM roles and permissions

- **Lambda execution role**: Grants Lambda permission to read and update DynamoDB.
- **API Gateway permissions**: Allows API Gateway to invoke the Lambda function.
- **S3 bucket policy**: Enables public read access to static files.
- **CORS configuration**: Ensures secure cross-origin requests between the custom domain and API Gateway.

---

### Cost Analysis

WIP
