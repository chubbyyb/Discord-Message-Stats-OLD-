import pandas as pd
import plotly.express as px

# Chop off the useless thing at the end
df = pd.read_csv('messages.csv')
df['Timestamp'] = df['Timestamp'].astype('str').str.slice(0,10)
df.to_csv(path_or_buf='new.csv')

# Print and sort the date only
df = pd.read_csv('new.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d')
df['Timestamp'].to_csv(path_or_buf='dates.csv')

df = pd.read_csv('dates.csv')
df1 = df.groupby('Timestamp').count().copy()
print(df.groupby('Timestamp').count().to_string())
print(df.mean(numeric_only=True,skipna = True))
fig = px.line(df1, title='Title')
fig.show()
