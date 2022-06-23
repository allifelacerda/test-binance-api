# doc - https://python-binance.readthedocs.io/en/latest/index.html
import json
from time import sleep
from binance.client import Client
from keys import api_key, api_secret

SYMBOL = 'BTCUSDT'
client = Client(api_key, api_secret)

while True:
    ticker = client.get_ticker(symbol=SYMBOL)
    json_obj = json.dumps(ticker, indent=4)
    print(json_obj)
    sleep(1)
