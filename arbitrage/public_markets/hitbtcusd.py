from arbitrage.public_markets._hitbtc import Hitbtc

class HitbtcUSD(Hitbtc):
    def __init__(self):
        super().__init__("USD","ETHUSD")

