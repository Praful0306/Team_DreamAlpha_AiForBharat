# Vidya-Setu: Step-by-Step AWS Deployment Guide 🚀🛰️

Follow these instructions to deploy your project to the AWS Cloud for the hackathon. These steps ensure you stay within the **Free Tier** and your **$20 budget**.

---

## 🏗️ Step 1: Create the DynamoDB Table
This is our "Neural Memory" that stores student progress and AI caches.

1.  Log in to the **AWS Console**.
2.  Search for **DynamoDB**.
3.  Click **Create table**.
4.  **Environment Variables for Backend (Lambda)**:
| Key | Value |
| :--- | :--- |
| **`MY_AWS_REGION`** | `us-east-1` |
| **`MY_AWS_ACCESS_KEY_ID`** | `...your primary key...` |
| **`MY_AWS_SECRET_ACCESS_KEY`** | `...your primary secret...` |
| **`CHAT_AWS_ACCESS_KEY_ID`** | `...your chat key...` |
| **`CHAT_AWS_SECRET_ACCESS_KEY`** | `...your chat secret...` |
| **`DYNAMODB_TABLE`** | `VidyaSetu_Progress` |
5.  **Partition key**: `PK` (String)
6.  **Sort key**: `SK` (String)
7.  **Table class**: Standard (Free tier eligible).
8.  **Capacity mode**: **On-demand** (Best for your budget - pay per request, $0 when idle).
9.  Click **Create table**.

---

## ⚡ Step 2: Deploy the Backend (AWS Lambda)
We will host your FastAPI code here.

1.  Search for **Lambda** in the AWS Console.
2.  Click **Create function**.
3.  **Function name**: `VidyaSetu-Backend`
4.  **Runtime**: **Python 3.12**
5.  **Architecture**: x86_64
6.  Click **Create function**.
7.  **Upload Code**:
    *   To run in Lambda, we need to include the "libraries" (FastAPI, Mangum, etc.).
    *   In your terminal (inside the `backend` folder), run:
        ```powershell
        pip install -r requirements.txt -t .
        ```
    *   Now, select the `app/` folder, `main.py`, and all the new library folders/files created by the command above.
    *   **Right-click -> Compress to ZIP file**.
    *   In the Lambda Console, click **Upload from** -> **.zip file** and select your ZIP.
8.  **Configuration**:
    *   Go to **Configuration** -> **General configuration** -> **Edit**.
    *   Change **Timeout** to **30 seconds** (needed for Bedrock response time).
    *   Click **Save**.
9.  **Runtime Settings**:
    *   Scroll down to **Runtime settings** -> **Edit**.
    *   Change **Handler** to `app.main.handler` (matches the Mangum handler we added).

---

## 🌐 Step 3: Connect API Gateway
This gives your Lambda function a URL so the frontend can talk to it.

1.  In your Lambda function, click **Add trigger**.
2.  Select **API Gateway**.
3.  **Intent**: **Create a new API**.
4.  **API type**: **HTTP API** (Cheaper and faster than REST API).
5.  **Security**: **Open** (We handle security in the code).
6.  Click **Add**.
7.  **Copy the "API Endpoint" URL** (e.g., `https://random-id.execute-api.us-east-1.amazonaws.com`). **You need this for the frontend!**

---

## 🚀 Step 4: Deploy the Frontend (AWS Amplify)
This hosts your React website.

1.  Search for **Amplify** in the AWS Console.
2.  Click **Create new app**.
3.  Choose **GitHub** and authorize your account.
4.  Select your `vidya-setu` repository.
5.  **Build settings**:
    *   Amplify will detect it's a monorepo. Set the **Root directory** to `frontend`.
6.  **Environment Variables**:
    *   Click **Advanced settings**.
    *   Add variable: `VITE_API_URL` = (Paste your API Gateway URL from Step 3).
7.  Click **Save and deploy**.

---

## 🔐 Step 5: Grant Permissions (IAM)
Lastly, we need to allow the Lambda function to talk to Bedrock and DynamoDB.

1.  In your Lambda function, go to **Configuration** -> **Permissions**.
2.  Click on the **Role name** (e.g., `vidya-setu-backend-role-xxxx`).
3.  In the IAM window, click **Add permissions** -> **Attach policies**.
4.  Search for and select:
    *   `AmazonBedrockFullAccess`
    *   `AmazonDynamoDBFullAccess`
5.  Click **Add permissions**.

---

**DONE!** Your app is now live in the cloud. Check the Amplify URL to see it in action! 🌌🧠
