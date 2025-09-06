
# 🚀 Flask on Kubernetes

This project demonstrates how to build, containerize, and deploy a simple **Flask web application** using:

- **Flask** (Python web framework)  
- **Docker** (containerization)  
- **Docker Compose** (multi-container setup with Nginx load balancing)  
- **Kubernetes** (orchestration with Deployment, Service, and Ingress)  
- **Nginx** (reverse proxy and load balancer)

The app exposes three endpoints:

- `/` → Home message  
- `/health` → Health check endpoint  
- `/details` → Shows hostname & pod IP (to verify load balancing)

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jkrishna77/flask-on-kubernetes.git
cd flask-on-kubernetes
````

---

## 2️⃣ Run Locally (Python Only)

Create a virtual environment, install dependencies, and run the Flask app:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/app.py
```

Now open in browser:

```
http://localhost:5000/
http://localhost:5000/health
http://localhost:5000/details
```

---

## 3️⃣ Run with Docker

Build the Docker image:

```bash
docker build -t flask-app .
```

Run the container:

```bash
docker run -p 5000:5000 flask-app
```

Test in browser:

```
http://localhost:5000/
http://localhost:5000/health
http://localhost:5000/details
```

---

## 4️⃣ Run with Docker Compose (3 Flask replicas + Nginx)

We have a **docker-compose.yml** that starts 3 instances of Flask (`flask1`, `flask2`, `flask3`) and an **Nginx reverse proxy** that load-balances traffic.

Start services:

```bash
docker-compose up --build
```

Open in browser:

```
http://localhost/
```

Each refresh of `/details` should show a different **hostname/IP**, proving that Nginx is load-balancing across Flask instances.

---

## 5️⃣ Deploy on Kubernetes (Minikube)

### Start Minikube

```bash
minikube start
minikube addons enable ingress
```

### Apply Kubernetes manifests

Note: Please add your dockerhub usesrname/image at deployment.yaml:spec.containers.image

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

### Verify resources

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

You should see 3 pods running (`flask-app`), a `flask-service` (ClusterIP), and an ingress (`flask-ingress`).

---

## 6️⃣ Access the App via Port Forwarding

Since we are on Minikube, we need to **port-forward** the Ingress controller to access from browser:

```bash
kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8080:80
```

Now open:

```
http://localhost:8080/
http://localhost:8080/health
http://localhost:8080/details
```

Each refresh of `/details` will show a **different pod hostname/IP**, confirming that Kubernetes is load-balancing traffic across replicas.

---

## 📊 Flow Diagram

### Docker Compose

```
[Browser] --> [Nginx Reverse Proxy] --> [Flask1 | Flask2 | Flask3]
```

### Kubernetes

```
[Browser] --> [Ingress Controller (Nginx)] --> [ClusterIP Service] --> [Flask Pods x3]
```

---

## ✅ Summary

* Local: Run Flask with Python.
* Docker: Containerize Flask.
* Docker Compose: Scale with multiple containers + Nginx load balancing.
* Kubernetes (Minikube): Deploy with Deployment, Service, Ingress → scale & manage at cluster level.


