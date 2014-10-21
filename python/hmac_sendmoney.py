"""
Example for using hmac for making API calls. Please see the HMAC
documentation at:

https://github.com/coinsph/api/wiki/Authentication-with-API-Key---Secret
"""
import requests
import hashlib
import hmac
import time
import json

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

body = {
    'currency': 'PHP',
    'btc_amount': 0.1,
    'payment_outlet': 'bdo',
    'bank_account_name': 'Customer bank account name',
    'bank_account_number': 'Customer bank account number',
}

url = 'https://coins.ph/api/v2/sellorder'

nonce = int(time.time() * 1e6)
if body is None:
    # For GET requests
    message = str(nonce) + url
else:
    # For POST requests
    body = json.dumps(body, separators=(',', ':'))
    message = str(nonce) + url + body
signature = hmac.new(str(API_SECRET), message, hashlib.sha256).hexdigest()

headers = {
    'ACCESS_SIGNATURE': str(signature),
    'ACCESS_KEY': API_KEY,
    'ACCESS_NONCE': nonce,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Use requests.get instead of POST for GET requests, without the data kwarg
response = requests.post(url, headers=headers, data=body)
