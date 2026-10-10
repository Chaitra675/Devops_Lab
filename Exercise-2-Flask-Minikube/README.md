# Exercise 2: Deploy a Flask App on Minikube Using kubectl and YAML

## 1. Objective

To learn Kubernetes fundamentals by deploying a Python Flask application on a local Minikube cluster using Docker and Kubernetes YAML configuration.

## 2. Tools and Technologies

- Python
- Flask
- Docker Desktop
- Minikube
- Kubernetes
- kubectl
- Visual Studio Code

## 3. Project Structure

```text
Exercise-2-Flask-Minikube/
├── app.py
├── Dockerfile
├── flask-deployment.yaml
├── README.md
└── screenshots/
    ├── flask-app-running.png
    └── image.png
```

## 4. Implementation

### Step 1: Start Minikube

Start the local Kubernetes cluster.

```powershell
minikube start --driver=docker
```

### Step 2: Create the Flask Application

The `app.py` file defines a Flask web application that returns a message when the home route is accessed.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
```

### Step 3: Create the Docker Image

The `Dockerfile` packages the Flask application and its dependency into a Docker image.

```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]
```

Build the image:

```powershell
docker build -t flask-app:latest .
```

Load the image into Minikube:

```powershell
minikube image load flask-app:latest
```

### Step 4: Create the Kubernetes Deployment and Service

The `flask-deployment.yaml` file defines a Deployment with one replica and a NodePort Service.

The Deployment runs the `flask-app:latest` image on container port `15000`. The Service forwards requests to the application.

### Step 5: Deploy the Application

Apply the Kubernetes configuration:

```powershell
kubectl apply -f flask-deployment.yaml
```

### Step 6: Verify the Deployment

Check the Deployment:

```powershell
kubectl get deployments
```

Check the Pods:

```powershell
kubectl get pods
```

Check the Services:

```powershell
kubectl get services
```

The Deployment should show one available replica, and the Flask Pod should reach the `Running` state.

### Step 7: Access the Flask Application

Generate a URL for the Service:

```powershell
minikube service flask-app-service --url
```

Open the generated URL in a browser.

Expected response:

```text
Hello from Flask on Kubernetes!
```

When using Minikube with the Docker driver on Windows, keep the terminal running if Minikube indicates it is required for the Service URL to work.

## 5. Screenshots

The `screenshots/` folder contains evidence of the Docker image and Kubernetes deployment.

- `flask-app-running.png`
- `image.png`

## 6. Result

The Flask application was packaged into a Docker image and deployed on a local Kubernetes cluster using a Kubernetes Deployment and NodePort Service.

The Deployment and Pod status were verified using `kubectl`, and the application was made accessible through the Minikube Service URL.

## 7. Conclusion

This exercise demonstrates how to containerize a Python Flask application using Docker, deploy it on Kubernetes using Minikube and YAML configuration, verify the Deployment and Service, and access the application through a generated URL.