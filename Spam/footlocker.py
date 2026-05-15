import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
cookies = {
    'localization': 'IL',
    'popup--closed': 'true',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://footlocker.co.il',
    'Referer': 'https://footlocker.co.il/',
    'Sec-CH-UA': '"Not-A.Brand";v="24", "Chromium";v="146"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

json_data = {
    'phoneNumber': phone_number,
    'uuid': 'd069072a-eca7-45a5-9d4d-a7b5719e7eba',
}

response = requests.post(
    'https://footlocker.co.il/apps/dream-card/api/proxy/otp/send',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
