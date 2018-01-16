import os
import hashlib
import hmac
import requests
import time


def get_last(phenny, input):
    secret_key = os.environ['BTC_SECRET']
    public_key = os.environ['BTC_PUB_KEY']

    timestamp = int(time.time())
    payload = '{}.{}'.format(timestamp, public_key)
    hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = '{}.{}'.format(payload, hex_hash)

    url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
    headers = {'X-Signature': signature}
    result = requests.get(url=url, headers=headers)
    last = str(round(float(result.json()["last"]), 2))

    phenny.say(last)
get_last.commands = ['btc']
get_last.priority = 'medium'



if __name__ == '__main__': 
    print __doc__.strip()
