# class Actions:
#     def __init__(self, df) -> None:
#         self.df = df

#     def decide_holding_stocks():
#         pass

#     def decide_new_stocks():
#         pass

import pandas as pd
import yfinance as yf
from module_technical_analysis import TechnicalAnalysis
import parameters

frame = pd.read_csv('Candidates_CSI300.csv')

def scan_candidates(frame):
    # positions, _, _ = module_scan_account.scan_account()

    potential_buy = []
    for ticker in frame['symbol']:

        # # For ticker in positions, we already did everything in Step 1.
        # if ticker in positions:
        #     continue

        # For other tickers, download data and run technical analysis for buy signals
        try:
            df = yf.download(ticker, start='2022-09-01')
            print(f'Running technical analysis on {ticker}...')
            ta = TechnicalAnalysis(df)
            ta.good_to_buy()

            if df['good_to_buy'][-1] == True:
                price = df['Close'][-1]
                if price * 100 >= parameters.total_equity * 0.2:
                    continue

                potential_buy.append((ticker, df['Close'][-1]))
        except:
            continue

    return potential_buy

# print(scan_candidates(frame))  


# from alpaca.trading.client import TradingClient
# import config
# import module_scan_account
# import module_scan_candidates
# from module_order import Order
# import pandas as pd
# from parameters import total_equity

# def decide_candidates():
#     tc = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)

#     # The bot would fire the same orders if yesterday was a holiday. 
#     # So if there are pending orders, do nothing. 
#     open_orders = tc.get_orders()
#     if len(open_orders) > 0:
#         return

#     # Get available equity
#     positions, num_positions, available_equity = module_scan_account.scan_account()

#     frame = pd.read_csv('candidates_Nasdaq.csv')
#     potential_buy = module_scan_candidates.scan_candidates(frame)
#     buy_plan = []

#     for new_ticker, new_ticker_price in potential_buy:
#         if available_equity / total_equity > 0.2:    
#             new_quantity = total_equity * 0.2 // new_ticker_price
#             if new_quantity > 0:
#                 place = Order(new_ticker, new_quantity)
#                 place.buy_order()  

#             buy_plan.append((new_ticker, new_ticker_price, new_quantity))
             
#     return buy_plan

# # print(decide_candidates())