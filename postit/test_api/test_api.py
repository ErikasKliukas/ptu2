from ast import And
import requests
from pprint import pprint

url = 'http://localhost:8000/api/'
headers = {'Authorization': "Token 90a5b2cc77b9cf87066119c4f2bf7f77c7bd6317"}
body = {
    'title': "testuojam per Python",
    'content': "lietingas antradienis, nesidziaugiu "
}

result = requests.post(url+'posts/',data=body, headers = headers)

if result.status_code == 200 and result.status_code < 204:
    print(result.json())
print(result.status_code)
