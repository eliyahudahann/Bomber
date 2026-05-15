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
    'Origin': 'https://itaybrands.co.il',
    'Referer': 'https://itaybrands.co.il/',
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
    'uuid': '046406c3-e7dd-4236-9728-d18a196c00e4',
}

response = requests.post(
    'https://itaybrands.co.il/apps/dream-card/api/proxy/otp/send',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
