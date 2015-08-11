"""
batch_sell_orders.py
~~~~~~~~~~~~~~~~~~~~

This module is a command line utility that allows processing of sell
orders by batch through a csv input file.

Usage:
$ batch_sell_orders.py input_csv_file.csv

Disclaimer:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

"""
import csv
import hashlib
import hmac
import time
import json
import requests
import sys
import argparse


class HMACRequestSignatureHandler(object):
    def __init__(self, api_secret='', body=''):
        self.api_secret = api_secret

    def get_nonce(self):
        """Return a nonce based on the current time.

        A nonce should only use once and should always be increasing.
        Using the current time is perfect for this.
        """
        return int(time.time() * 1e6)

    def __call__(self, url, nonce=None, body=None):
        """Return an HMAC signature based on the request."""
        if nonce is None:
            nonce = self.get_nonce()
        if body is None:
            # GET requests don't have a body, so we'll skip that for signing
            message = str(nonce) + url
        else:
            body = json.dumps(body, separators=(',', ':'))
            message = str(nonce) + url + body

        return str(
            hmac.new(
                str(self.api_secret),
                message,
                hashlib.sha256
            ).hexdigest()
        )


class SellOrderApi(object):
    def __init__(self, api_key='', api_secret=''):
        self.url = 'https://coins.ph/api/v2/sellorder'
        self.api_key = api_key
        self.api_secret = api_secret
        self.hmac_handler = HMACRequestSignatureHandler(
            api_secret=self.api_secret
        )

    def sign_request(self, nonce, body):
        return self.hmac_handler(
            self.url,
            nonce=nonce,
            body=body
        )

    def post(self, body):
        nonce = self.hmac_handler.get_nonce()
        signature = self.sign_request(nonce, body)
        headers = {
            'ACCESS_SIGNATURE': signature,
            'ACCESS_KEY': self.api_key,
            'ACCESS_NONCE': nonce,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        body = json.dumps(body, separators=(',', ':'))
        return requests.post(self.url, headers=headers, data=body).json()


class SellOrderCSVParser(object):
    def __init__(self, filename):
        self.filename = filename

    def __call__(self):
        parsed_orders = []
        count = 0
        with open(self.filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = []
            for row in reader:
                if count == 0:
                    header = row
                    count += 1
                    continue
                data = {}
                for field, value in zip(header, row):
                    data[field] = value
                parsed_orders.append(data)
        return parsed_orders


def process_requests(config, filename):
    with open(config) as config:
        config = json.loads(config.read())
    parser = SellOrderCSVParser(filename=filename)
    api = SellOrderApi(
        api_key=config['api_key'],
        api_secret=config['api_secret']
    )
    results = []
    for body in parser():
        bank_account_name = body['bank_account_name']
        print 'Creating a sell order for bank account {}'.format(
            bank_account_name
        )
        result = api.post(body)
        if 'errors' in result:
            print 'Error creating sell order for bank account {}'.format(
                bank_account_name
            )
        else:
            print 'Created sell order {} for {}'.format(
                result['order']['id'],
                bank_account_name
            )


def main():
    arg_parser = argparse.ArgumentParser(
        description='Batch process sell orders provided by a csv file'
    )
    arg_parser.add_argument('filename', nargs=1, type=str)
    arg_parser.add_argument('--config', default='config.json', type=str)
    args = arg_parser.parse_args()
    process_requests(args.config, args.filename[0])


if __name__ == '__main__':
    main()
