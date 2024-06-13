from prometheus_client import start_http_server, Summary
import time

# Create a metric to track time spent processing requests and a count of requests for monitoring.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

def start_metrics_server():
    start_http_server(8000)
    while True:

        time.sleep(1)

if __name__ == '__main__':
    start_metrics_server()
