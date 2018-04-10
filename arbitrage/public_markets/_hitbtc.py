from arbitrage.public_markets.market import Market
from new_base.hitbtc_rest import Client

class Hitbtc(Market):
    def __init__(self,currency, code):
        super().__init__(currency)
        self.code = code
        self.update_rate = 20

    def update_depth(self):
        public_key = "a9b6cdaa73d1005a0da78e27d55e6703"
        secret = "f1b37b20f9ec1e91fc61e7747da4427c"
        client = Client("https://api.hitbtc.com", public_key, secret)

        self.depth = self.format_depth(client.get_orderbook(self.code))

    def sort_and_format(self, l, reverse):
        r = []
        for i in l:
            r.append({'price': float(i['price']), 'amount': float(i['size'])})
        r.sort(key=lambda x: float(x['price']), reverse=reverse)
        return r

    def format_depth(self, depth):
        bids = self.sort_and_format(depth['bid'], True)
        asks = self.sort_and_format(depth['ask'], False)
        return {'asks': asks, 'bids': bids}

if __name__ == "__main__":
    client = Hitbtc('USD','ETHUSD')
    client.update_depth()
    print(client.depth)