import requests


def run(query):
    return requests.post("http://localhost:8000/run", json={"query": query}).json()
