FROM python:alpine3.16
WORKDIR /efrei-devops-tp2
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3","meteo.py"]
