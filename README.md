# python_flask_docker
Hello World python_flask for docker

# Docker Build Image
docker build -t flaskapp .

# Docker Run
docker run -p 5000:5000 --name python_flask flaskapp

# Deploy using Kubernetes
kubectl apply -f deployment.yaml
