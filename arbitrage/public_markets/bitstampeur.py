from arbitrage.public_markets._bitstamp import Bitstamp

class BitstampEUR(Bitstamp):
    def __init__(self):
        super().__init__("EUR", "etheur")

if __name__ == "__main__":
    market = BitstampEUR()
    market.update_depth()
    print(market.get_ticker())
