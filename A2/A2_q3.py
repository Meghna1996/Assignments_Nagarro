import json
import requests

#api1
url1 = 'https://www.purgomalum.com/service/json?text=this is some test input'
response = requests.get(url1)
data = response.json()
print(f"Data fetch from api1: \n {data}")

with open('api_data1.json','w') as f:
    f.write(json.dumps(data))

#api2
url2 = 'https://api.carbonintensity.org.uk/intensity'
headers = {
    'Accept': 'application/json'
}
response = requests.get(url2, params={}, headers = headers)
data = response.json()
print(f"Data fetch from api2: \n {data}") 

with open('api_data2.json','w') as f:
    f.write(json.dumps(data))
