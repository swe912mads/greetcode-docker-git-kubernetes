FROM python:3.13-slim

WORKDIR /create-kubernetes

COPY requirements.txt .

COPY kube.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "kube.py"]