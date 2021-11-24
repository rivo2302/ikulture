import requests
import json
API_URL = 'http://localhost:8000'
response = requests.get(f'{API_URL}/commune')
data = json.loads(response.text)

for a in data :
    print(a)
    break