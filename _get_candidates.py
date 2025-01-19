import pandas as pd

df = pd.read_csv('Fundamentals_CSI300.csv', index_col='symbol')
filt =  (df['marketCap'] >= 70_000_000_000) & \
        (df['trailingEps'] <= 60) & \
        (df['returnOnEquity'] >= 0.1) & \
        (df['profitMargins'] >= 0.2)
df = df.loc[filt]

df.to_csv('Candidates_CSI300.csv')
print("Candidates updated!")