import os
import hashlib
import hmac
import requests
import time


last_btc = 0

def get_last(phenny, input):
    secret_key = os.environ['BTC_SECRET']
    public_key = os.environ['BTC_PUB_KEY']
    global last_btc

    timestamp = int(time.time())
    payload = '{}.{}'.format(timestamp, public_key)
    hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = '{}.{}'.format(payload, hex_hash)

    url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
    headers = {'X-Signature': signature}
    try:
        result = requests.get(url=url, headers=headers)
        last_rounded = round(float(result.json()["last"]), 2)
	last = str(last_rounded)
	if last_rounded > last_btc:
		last += "! BUY BUY BUY!"
	if last_rounded < last_btc:
		last += "! SELL SELL SELL!"

	last_btc = last_rounded

    except Exception as e:
        last = "bark bark?!"
        print(e)

    phenny.say(last)
get_last.commands = ['btc']
get_last.priority = 'medium'



if __name__ == '__main__': 
    print __doc__.strip()
