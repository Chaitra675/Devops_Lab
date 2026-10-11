# Exercise 3: Scaling Flask App Using Kubernetes ReplicaSets

## 1. Objective

- Understand Kubernetes ReplicaSets and Pods.
- Scale a Flask application from three replicas to five replicas.
- Observe Pod distribution across a single node.
- Verify automatic Pod replacement when a Pod is deleted.
- Understand scalability and resiliency in a flash-sale application.

## 2. Real-Life Use Case: E-Commerce Flash Sale

During an e-commerce flash sale, incoming requests can increase rapidly. Running multiple replicas of an application helps Kubernetes maintain several copies of the application.

This exercise simulates a flash-sale service with endpoints for viewing the sale, placing a simulated buy order, and checking application health.

## 3. Technologies Used

- Python and Flask
- Docker
- Minikube
- Kubernetes
- kubectl
- YAML
- Visual Studio Code

## 4. Project Structure

```text
Exercise-3-Flask-ReplicaSet/
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
├── README.md
└── screenshots/
    ├── 03-replicas.png
    ├── 05-five-replicas.png
    └── flash-scale-flask-appln.png
```

## 5. Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays the Big Sale welcome message and serving Pod name. |
| `/buy?user=123` | Simulates a purchase and returns the product, user, and serving Pod. |
| `/health` | Returns the application's health status and Pod name. |

## 6. Implementation Steps

### Step 1: Start Minikube

```powershell
minikube start --driver=docker
```

### Step 2: Build the Docker Image

```powershell
docker build -t flashsale:1.0 .
```

Load the image into Minikube:

```powershell
minikube image load flashsale:1.0
```

### Step 3: Deploy the ReplicaSet and Service

```powershell
kubectl apply -f flashsale-replicaset.yaml
```

### Step 4: Verify the Initial Replicas

```powershell
kubectl get rs
kubectl get pods -l app=flashsale
kubectl get services
```

Initially, the ReplicaSet is configured to maintain three replicas.

### Step 5: Scale to Five Replicas

```powershell
kubectl scale rs flashsale-rs --replicas=5
```

Verify the updated replica count:

```powershell
kubectl get rs
kubectl get pods -l app=flashsale
```

### Step 6: Test Automatic Pod Recovery

Delete one Pod using its actual name:

```powershell
kubectl delete pod <pod-name>
```

Verify the Pods again:

```powershell
kubectl get pods -l app=flashsale
```

The ReplicaSet creates a replacement Pod to maintain the desired count of five replicas.

### Step 7: Access the Application

```powershell
minikube service flashsale-svc --url
```

Open the generated URL in a browser. Test the homepage, buy endpoint, and health endpoint.

On Windows with the Docker driver, keep the terminal open if Minikube requires it for the service URL to work.

## 7. Key Observations and Learnings

- **Pod scaling:** Kubernetes can increase the number of application replicas from three to five.
- **Resiliency:** The ReplicaSet replaces a deleted Pod to maintain the desired replica count.
- **Resource efficiency:** Replicas can be adjusted according to workload requirements.
- **Health monitoring:** Readiness and liveness probes check the application's health endpoints.
- **Service discovery:** The Kubernetes Service routes requests to Pods matching its selector.

## 8. Result

The Flash Sale Flask application was deployed on Minikube using a Docker image, Kubernetes ReplicaSet, and Service. The application was scaled from three to five replicas, and automatic Pod replacement was observed after deleting a Pod.

## 9. Conclusion

This exercise demonstrates Kubernetes ReplicaSet management, replica scaling, health checks, Service access, and automatic Pod recovery in a simulated e-commerce flash-sale application.