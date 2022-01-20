import requests
import json

def check_appropriate(text):
    url = "http://143.248.41.54:8000/predict"
    data = json.dumps({"text":text})
    result = json.loads(requests.post(url=url, data=data).text)
    return result
    