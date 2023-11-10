import pandas as pd
from urllib.request import urlretrieve
import os

#Get data from stooq
ticker = 'ETH.V'
interval = 'd'
url = f'https://stooq.com/q/d/l/?s={ticker}&i={interval}'
csv_file = ticker + '.csv'
urlretrieve(url, csv_file)

#Data = pandas read of csv file specific collumns
priceAndVolume = pd.read_csv(csv_file)[["Date","Close","Volume"]]
os.remove(csv_file)

# #Rename collumns
priceAndVolume = priceAndVolume.rename(columns={'Close': 'Price'})
#Format the Date collum as pandas datetime
priceAndVolume["Date"] = pd.to_datetime(priceAndVolume["Date"])
#Remove values of absolute 0
priceAndVolume = priceAndVolume[priceAndVolume["Price"] > 0]

#Sort Values by date
priceAndVolume.sort_values(by="Date", inplace=True)


# #Export pandas to csv
# df.to_csv(r"/home/rupx/Documents/Finance/CVS/FREE/eth.csv")

#print(priceAndVolume)

# # Exclude data from the dataframe by index
# #df = df[df.index > 800]

# # Exclude data from the dataframe by index YY-MM-DD
# #df = df[df.Date >= "1971"]
# #df = df[df.Date <= "2020-03-03"]

# df.reset_index(inplace=True)
# df = df.drop(['index'], 1)


