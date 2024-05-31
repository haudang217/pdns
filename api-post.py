import requests
import json

url = 'http://192.168.10.100:8081/api/v1/servers/localhost/zones/ttepz.core'
headers = {
    'X-API-Key': 'SXpFTVQ3c04wYVNoRlh3',
    'Content-Type': 'application/json'
}
data = {
    "name": "example.org.",
    "kind": "Native",
    "masters": [],
    "nameservers": ["ns1.example.org.", "ns2.example.org."]
}

data_json = json.dumps(data)

# Sử dụng PUT nếu tài liệu chỉ ra rằng đó là phương thức cần thiết
response = requests.put(url, headers=headers, data=data_json)

print(response.status_code)
print(response.text)
