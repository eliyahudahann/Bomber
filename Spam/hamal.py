import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
cookies = {
    'vad-loc-code': 'il',
    'userUniqueId': 'f0cf88b7-1fc2-43d8-a4c8-32456108ddce_1778595042670',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://hamal.co.il',
    'Referer': 'https://hamal.co.il/',
    'Sec-CH-UA': '"Not-A.Brand";v="24", "Chromium";v="146"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

json_data = {
    'value': phone_number,
    'type': 'phone',
    'projectId': '1',
}

response = requests.post('https://users-auth.hamal.co.il/auth/send-auth-code', cookies=cookies, headers=headers, json=json_data)

