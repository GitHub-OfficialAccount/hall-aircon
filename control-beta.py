import requests,json

url = 'https://apintu-prod.daikinpayu.com/v2/ac/control'

headers = {
    'User-Agent': 'Dart/3.0 (dart:io)',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Authorization': 'Bearer <token>'
}

data = {
    # 'setpoint': '16'
    # 'power': '0'
}

response = requests.post(url, headers=headers, data=data)

print('Status Code:', response.status_code)

print('Response:', json.dumps(response.json(), indent=4))