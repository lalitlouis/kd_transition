import requests
import sys

BASE_URL = sys.argv[1].rstrip("/")


URL = "{}/v1/models/tfjob-serving:predict".format(BASE_URL)
DATA = {  
  "instances":[[1.91518414, 1.14995454, -1.52847073, 0.79430654]]
}

session = requests.Session()
responce = session.post(URL, json=DATA, allow_redirects=False)

print(responce.status_code)
print(responce.json())
