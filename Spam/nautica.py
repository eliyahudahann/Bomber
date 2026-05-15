import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
cookies = {
    'form_key': '2ft43mH4jAuX3jtX',
    'PHPSESSID': 'jq0bj11vr8ffr5v7s76vlbb5a5',
    'store': 'default',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.nautica.co.il',
    'Referer': 'https://www.nautica.co.il/',
    'Sec-CH-UA': '"Not-A.Brand";v="24", "Chromium";v="146"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'form_key': '2ft43mH4jAuX3jtX',
    'bot_validation': '1',
    'type': 'login',
    'telephone': phone_number,
    'code': '',
    'compare_email': '',
    'compare_identity': '',
}

response = requests.post('https://www.nautica.co.il/customer/ajax/post/', cookies=cookies, headers=headers, data=data)