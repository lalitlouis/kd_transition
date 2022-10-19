import json
import requests
import sys


BASE_URL = sys.argv[1].rstrip("/")


URL = "{}/api/v1.0/predictions".format(BASE_URL)

DATA = {
    "data": {
        "ndarray": [
            [1.91518414, 1.14995454, -1.52847073, 0.79430654]
        ]
    }
}

data_string = json.dumps(DATA)

session = requests.Session()
responce = session.post(url=URL, data=[("json", data_string)])

print(responce.text)