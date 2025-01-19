import module_technical_analysis
import yfinance as yf

def decide_holding_stocks():
    holding_stocks = ['600196.ss']

    result = []
    for stock in holding_stocks:
        df = yf.download(stock, start='2022-09-01')
        ta = module_technical_analysis.TechnicalAnalysis(df)
        ta.good_to_sell()

        if df['good_to_sell'][-1] == True:
            result.append((stock, 'Sell'))
        else:
            result.append((stock, 'No action'))
    
    return result

# print(decide_holding_stocks())

