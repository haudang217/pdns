import requests

url = 'http://192.168.10.100:8081/api/v1/servers/localhost/zones/example.org'
headers = {'X-API-Key': 'SXpFTVQ3c04wYVNoRlh3'}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print('Failed to fetch data. Status code:', response.status_code)
