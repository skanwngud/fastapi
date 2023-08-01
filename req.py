import requests
import json

resp = requests.post(
    url="http://127.0.0.1:8080",
    data=json.dumps({"model_name": "model name test!"})
)

resp = json.loads(resp.text)
print(resp)