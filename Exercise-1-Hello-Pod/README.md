# Exercise 1: Hello Pod — Kubernetes

## Aim
To deploy an Nginx container as a Pod in Kubernetes using Minikube and expose it through a NodePort Service.

## Tools Used
- Docker Desktop
- Minikube
- Kubernetes
- kubectl
- Visual Studio Code

## Procedure

### Step 1: Start Minikube
```powershell
minikube start --driver=docker
```

### Step 2: Deploy the Pod
```powershell
kubectl apply -f pod.yaml
```

### Step 3: Verify the Pod
```powershell
kubectl get pods
```

### Step 4: Expose the application
```powershell
kubectl apply -f service.yaml
```

### Step 5: Verify the Service
```powershell
kubectl get services
```

### Step 6: Access the application
```powershell
minikube service hello-k8s
```

## Expected Result
- The Kubernetes node is Ready.
- The Nginx Pod reaches Running status.
- The NodePort Service is created.
- The Nginx welcome page opens in the browser.

## Conclusion
Successfully deployed an Nginx container in a Kubernetes Pod using Minikube and exposed the application through a NodePort Service.

## Screenshots
The `screenshots` folder contains evidence of the running Nginx application. Add screenshots of the Pod and Service status before submission.