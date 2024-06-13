# bbcs-2024
LDSS (Legal Decision Support System)

## Overview
For our Legal Decision Support System, we propose a multi-service application utilizing various technologies including Ruby (using Sinatra) and Python (using FastAPI). To ensure a safe, self-sustaining, and stable deployment, we use Docker for containerization, Logstash and ElasticSearch for logging, Prometheus and Grafana for monitoring, and a Streamlit application for querying a Generative AI model from Google Cloud.

## Services
Ruby app: 
A Sinatra application that logs messages in JSON format and exposes a few endpoints and RSpec tests for unit testing. Some dependencies include:
- sinatra
- rackup
- rspec
- rack-test

Applications:
Our FastAPI applications expose an endpoint for creating items and instrumented with Prometheus metrics, where Prometheus is used for scraping metrics from the services. Afterwards, Grafana is used for visualizing the metrics collected by Prometheus. Logstash collects logs from the services and forwards them to ElasticSearch. To query the Generative AI model from Google Cloud, we utilize a Streamlit application.

## setup instructions 
Under the app folder, put client_secret.json for authentication (contect Simul-Eqn for file) 
On first run, it will ask for authorization. Please log in to the agreed upon gmail account to access it. 

## running instructions 
1. Clone the repository
git clone <repository_url>
cd LDSS

2. Build and start the services using Docker Compose:
docker-compose up --build

Streamlit app: To run the app, go into the app directory, and enter in a terminal "streamlit run app.py"

Access the services: 
Ruby App: http://localhost:4567 
Service 1: http://localhost:8000 
Service 2: http://localhost:8002 
Prometheus: http://localhost:9090 
Grafana: http://localhost:3000 
Kibana: http://localhost:5601

To run unit tests for the Ruby app:
docker-compose run ruby_app rspec

## Notes

Ensure Docker is installed on your system
