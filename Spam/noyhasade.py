import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
cookies = {
    '_ga': 'GA1.1.2066503503.1778597019',
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://noyhasade.co.il',
    'Referer': 'https://noyhasade.co.il/',
    'Sec-CH-UA': '"Not-A.Brand";v="24", "Chromium";v="146"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

params = {
    'origin': 'web',
}

json_data = {
    'phone': phone_number,
    'email': False,
    'ip': None,
}

response = requests.post('https://api.noyhasade.co.il/api/login', params=params, cookies=cookies, headers=headers, json=json_data)
