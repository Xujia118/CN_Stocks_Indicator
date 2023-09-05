import yfinance as yf
import pandas as pd
import os

wiki = 'https://zh.wikipedia.org/zh-cn/%E6%B2%AA%E6%B7%B1300'
CSI_300 = pd.read_html(wiki)[1]['代码'].astype(str).str.zfill(6).to_list()

def get_tickers_list(tickers):
    ticker_list = []

    for ticker in tickers:
        if ticker[0] == '6':
            ticker = ticker + '.ss'
        else:
            ticker = ticker + '.sz'
        ticker_list.append(ticker)

    return ticker_list

def get_financials():
    ticker_list = get_tickers_list(CSI_300)
    
    csv_file = 'Fundamentals_CSI300.csv'
    write_headers = not os.path.isfile(csv_file)

    for ticker in ticker_list:
        try:
            infos = yf.Ticker(ticker).info
            df = pd.json_normalize(infos)
            df = df.set_index('symbol')

            fundamentals = ['marketCap',
                            'trailingPE', 
                            'trailingEps',             
                            'returnOnEquity',
                            'profitMargins',
                            'dividendYield'
                            ]

            df = df[fundamentals]
            df.to_csv('Fundamentals_CSI300.csv', mode='a', header=write_headers)
            write_headers=False
        except:
            continue

    print("Financial data has been written to the CSV file.")
    return 

get_financials()