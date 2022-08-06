import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"
get_response = requests.get(endpoint, json ={"query":"Hello world"}) # HTTP Request 
print(get_response.json())

# print(get_response.text) # prints raw text response
# print(get_response.status_code)
