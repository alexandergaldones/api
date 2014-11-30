import hashlib, hmac, time, json, os, sys
import requests
import argparse


def main():
    global args
    parser = argparse.ArgumentParser(description='Coins funds transfer.')
    parser.add_argument('target_address',
                        help='Target email, phone or bitcoin address')
    parser.add_argument('amount', help='Amount of BTC to send')
    parser.add_argument('--key', help='Client Key. Defaults to COINS_API_KEY in environment',
                        default=os.environ.get('COINS_API_KEY'))
    parser.add_argument('--secret', help='Shared Secret.  Defaults to COINS_API_SECRET in environment',
                        default=os.environ.get('COINS_API_SECRET'))
    parser.add_argument('--server', help='Coins.ph server to use.  Defaults to https://coins.ph',
                        default="https://coins.ph")
    args = parser.parse_args()

    print send_bitcoin(args.target_address, args.amount)


def make_request(url, body=''):
    """Make a HMAC request to coins"""
    nonce = str(int(time.time()))

    if body:
        body = json.dumps(body, separators=(',', ':'))
    message = nonce + url + body

    # Generate an hmac using the message
    signature = hmac.new(
        args.secret,
        message,
        hashlib.sha256
    ).hexdigest()

    headers = {
        'ACCESS_SIGNATURE': signature,
        'ACCESS_KEY': args.key,
        'ACCESS_NONCE': nonce,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        if body:
            response = requests.post(url, headers=headers, data=body)
        else:
            response = requests.get(url, headers=headers)
        result = response.json()
        if "errors" in result:
            raise RuntimeError()
        return result
    except requests.ConnectionError:
        print "Unable to connect to {}".format(url)
        sys.exit(1)
    except ValueError:
        print "Unable to parse response:\n{}".format(response.text)
        print "Status Code {}".format(response.status_code)
        sys.exit(1)
    except RuntimeError:
        print "Server says:\n{}".format(result)
        sys.exit(1)


def get_my_account():
    return make_request(
        "{}/d/api/crypto-accounts/?currency=BTC".format(args.server)
    )['crypto-accounts'][0]


def send_bitcoin(target_address, amount):
    return make_request(
        "{}/d/api/crypto-payments/".format(args.server),
        body=dict(
            target_address=target_address,
            amount=amount,
            account=get_my_account()['id']
        )
    )

if __name__ == "__main__":
    main()
