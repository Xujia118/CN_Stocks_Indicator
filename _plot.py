import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
from module_technical_analysis import TechnicalAnalysis

engine = sqlalchemy.create_engine('sqlite:///CSI_300.db')

start_date = '2022-01-01'
ticker = '600196.ss'

sql_query = f"SELECT * FROM '{ticker}' WHERE Date >= '{start_date}'"
df = pd.read_sql(sql_query, engine)

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date
df.set_index('Date', inplace=True)

ta = TechnicalAnalysis(df)

# ta.Bollinger() 
# plt.plot(df[['Close', 'SMA20', 'Upper', 'Lower']])
# plt.scatter(df.index[df['Boll_buy']], df[df['Boll_buy']]['Close'], marker='^', color='g')
# plt.scatter(df.index[df['Boll_sell']], df[df['Boll_sell']]['Close'], marker='v', color='r')
# plt.fill_between(df.index, df['Upper'], df['Lower'], color='grey', alpha=0.3)
# plt.legend(['Close', 'SMA20', 'Upper', 'Lower'])

# ta.SMA120()
# print(df.tail(120))
# plt.plot(df[['Close', 'SMA120']])

# ta.buy_consolidation()
# ta.sell_consolidation()
# plt.scatter(df.index[df['buy_consolidation']], df[df['buy_consolidation']]['Close'], marker='^', c='g')
# plt.scatter(df.index[df['sell_consolidation']], df[df['sell_consolidation']]['Close'], marker='^', c='r')
# plt.plot(df['Close'], c='k', alpha=0.1)

# my_date = '2021-10-13'
# print(df['Small_candle'].loc[my_date])
# print(df['Bullish_engulf'].loc[my_date])

ta.good_to_buy()
ta.good_to_sell()

# print(df['good_to_buy'].value_counts())
# print(df['good_to_sell'].value_counts())

# print(df.loc['2022-09-29'])

plt.scatter(df.index[df['good_to_buy']], df[df['good_to_buy']]['Close'], marker='^', c='g')
plt.scatter(df.index[df['good_to_sell']], df[df['good_to_sell']]['Close'], marker='v', c='r')
plt.plot(df[['Close', 'SMA60']], c='k', alpha=0.1)
plt.show()



