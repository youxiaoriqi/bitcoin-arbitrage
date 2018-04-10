from arbitrage.public_markets._bitstamp import Bitstamp

class BitstampUSD(Bitstamp):
    def __init__(self):
        super().__init__("USD", "ethusd")

if __name__ == "__main__":
    market = BitstampUSD()
    market.update_depth()
    print(market.get_ticker())
