FROM python:3.13-slim

WORKDIR /create-kubernetes

COPY kube.py .

CMD ["python", "kube.py"]