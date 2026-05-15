import requests
import sys 
phone_number = sys.argv[1] if len(sys.argv) > 1 else "0528357402"
cookies = {
    'form_key': 'ob8IF9pBo2dpQBgk',
    'PHPSESSID': '8urgeh1b2u516p3csqsu358npi',
    'store': 'default',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.urbanica-wh.com',
    'Referer': 'https://www.urbanica-wh.com/',
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
    'form_key': 'ob8IF9pBo2dpQBgk',
    'bot_validation': '1',
    'type': 'login',
    'telephone': phone_number,
    'code': '',
    'compare_email': '',
    'compare_identity': '',
}

response = requests.post('https://www.urbanica-wh.com/customer/ajax/post/', cookies=cookies, headers=headers, data=data)