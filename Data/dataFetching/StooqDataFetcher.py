import pandas as pd
from urllib.request import urlretrieve
import os
from Data.Assets import assets


class StooqDataFetcher:
    def __init__(self, interval='d'):
        self.interval = interval

    def fetch_historical_data(self, crypto):
        url = f'https://stooq.com/q/d/l/?s={crypto.stooq}&i={self.interval}'
        csv_file = f"{crypto.code}.csv"
        urlretrieve(url, csv_file)

        try:
            # Attempt to read specific columns from the CSV file
            try:
                price_and_volume = pd.read_csv(csv_file)[["Date", "Close"]]
            except KeyError as e:
                print(f"Error: CSV file for {crypto.name} does not contain expected columns. {e}")
                return None

            # Rename columns
            price_and_volume = price_and_volume.rename(columns={'Close': 'Price'})
            # Format the 'Date' column as pandas datetime
            price_and_volume["Date"] = pd.to_datetime(price_and_volume["Date"])
            # Remove rows where 'Price' is 0
            price_and_volume = price_and_volume[price_and_volume["Price"] > 0]
            # Sort by 'Date'
            price_and_volume.sort_values(by="Date", inplace=True)
        finally:
            # Remove the CSV file
            os.remove(csv_file)

        return price_and_volume

# Create a single StooqDataFetcher instance
data_fetcher = StooqDataFetcher()

# Fetch and store historical data for all cryptocurrencies
historical_data = {}
for asset in assets:
    historical_data[asset.name] = data_fetcher.fetch_historical_data(asset)
    historical_data[asset.name].to_csv(fr"/home/ruepa/FinancialData/Data/{asset.group}/{asset.name}.csv")
    #print(f"Data for {crypto.name}:")
    #print(historical_data[crypto.name])
    #print("\n")