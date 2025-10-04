# Awesome DevOps Platform

A microservices-based e-commerce platform demonstrating Catalog and Orders services deployed on Kubernetes with Docker containers. This project showcases microservices architecture, containerization, scaling, and service-to-service communication.

## Table of Contents
- Project Overview
- Technologies Used
- Architecture
- Setup and Installation
- Running the Services
- Scaling and Testing
- API Endpoints
- Author

## Project Overview
This project contains two main services: Catalog Service – Provides product information (CRUD operations) and Orders Service – Consumes the Catalog service to fetch products. The services are containerized using Docker, deployed in Kubernetes, and scaled horizontally to demonstrate load balancing.

## Technologies Used
Python 3.11 & Flask, Docker & Docker Compose, Kubernetes (kubectl), Git & GitHub

## Architecture
Orders Pod queries Catalog Service, which is backed by multiple Catalog Pods. Catalog service is exposed internally in the Kubernetes cluster, and horizontal scaling is implemented to show load balancing.

## Setup and Installation
1. Clone the repository:
git clone https://github.com/wilson7777777/awesome-devops-platform.git
cd awesome-devops-platform
2. Build Docker images:
docker build -t catalog-image:latest .
docker build -t orders-image:latest -f Dockerfile.orders .
3. Deploy to Kubernetes:
kubectl apply -f k8s/catalog-deployment.yaml
kubectl apply -f k8s/orders-deployment.yaml
4. Check pods:
kubectl get pods -w

## Running the Services
After deployment, execute commands from the Orders pod to test connectivity with Catalog service:
kubectl exec -it <orders-pod-name> -- bash
curl http://catalog:80/
curl http://catalog:80/products

## Scaling and Testing
Scale Catalog service horizontally:
kubectl scale deployment/catalog --replicas=5
kubectl get pods -w
Perform multiple requests to demonstrate load balancing:
for i in {1..10}; do curl -s http://catalog:80/products; echo ""; done
You will see requests served by different Catalog pods.

## API Endpoints
Catalog Service:
GET / – Returns service status and pod name
GET /products – Returns list of all products
GET /products/<id> – Returns single product by ID
POST /products – Add a new product
PUT /products/<id> – Update an existing product
DELETE /products/<id> – Delete a product

## Author
Wilson Nnebi  
GitHub: https://github.com/wilson7777777  
Email: wilsononline2@yahoo.com

**Project Status:** Completed and fully functional on Kubernetes

