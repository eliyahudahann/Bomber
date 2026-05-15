import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
headers = {
    'Host': 'webapi.mishloha.co.il',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://www.mishloha.co.il',
    'Referer': 'https://www.mishloha.co.il/',
    'Sec-CH-UA': '"Not-A.Brand";v="24", "Chromium";v="146"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

params = {
    'uuid': 'c049beda-2a99-442c-afa9-db86ea140940',
    'apiKey': 'BA6A19D2-F5BD-4B75-A080-6BD1E2FBEF54',
    'sessionID': 'd04562ae-09d6-a142-40ac-3e769e0b3290',
    'culture': 'he',
    'apiVersion': '2',
}

json_data = {
    'phoneNumber': phone_number,
    'sourceFrom': 'desktopHomePage',
    'sessionID': 'd04562ae-09d6-a142-40ac-3e769e0b3290',
}

response = requests.post(
    'https://webapi.mishloha.co.il/api/profile/sendSmsVerificationCodeByPhoneNumber',
    params=params,
    headers=headers,
    json=json_data,
)
