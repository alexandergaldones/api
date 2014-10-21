"""
Example for using oauth for making API calls. Please see the OAuth2
documentation at:

https://github.com/coinsph/api/wiki/Authentication-with-client-a-token-OAuth2
"""
import requests
import time

TOKEN = 'yourtoken'

body = {
    'currency': 'PHP',
    'btc_amount': 0.1,
    'payment_outlet': 'bdo',
    'bank_account_name': 'Customer bank account name',
    'bank_account_number': 'Customer bank account number',
}

url = 'https://coins.ph/api/v2/sellorder'
nonce = int(time.time() * 1e6)

headers = {
    'Authorization': 'Bearer {}'.format(TOKEN),
    'ACCESS_NONCE': nonce,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept': 'application/json'
}

# Use requests.get instead of POST for GET requests, without the data kwarg
response = requests.post(url, headers=headers, data=body)
