from alpaca.trading.client import TradingClient
from alpaca.data import OptionHistoricalDataClient
from alpaca.trading.requests import GetAssetsRequest
import pandas as pd


class AlpacaOptions:

    def __init__(self, keys):
        self.__option_client = OptionHistoricalDataClient(keys[0], keys[1])
        self.__trading_client = TradingClient(keys[0], keys[1])

    def get_all_options(self):
        req = GetAssetsRequest(
          attributes="options_enabled",
        )
        assets = self.__trading_client.get_all_assets(req)
        investable_universe = [asset.symbol for asset in assets if asset.tradable and asset.easy_to_borrow\
                               and asset.fractionable and asset.shortable]
        return investable_universe


if __name__ == "__main__":
    keys = ["PK63EMCGHNEWJTXMVH00",  "71apnYcpN6j5Mc9qGdEjPpnd1csGIz3q0yM1uhIc"]
    App = AlpacaOptions(keys)
    tickers_w_options = App.get_all_options()
    df = pd.DataFrame({"Ticker with options": tickers_w_options})
    df.to_csv("Ticker_w_Options_Alpaca.csv")
    x = 0
