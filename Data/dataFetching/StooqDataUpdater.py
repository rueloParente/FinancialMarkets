import pandas as pd
from datetime import datetime, timedelta
from urllib.request import urlretrieve
import os
from Data.Assets import assets


def update_data_with_stooq(local_csv_path, stooq_ticker):
    # Load the local historical data
    df = pd.read_csv(local_csv_path)
    df["Date"] = pd.to_datetime(df["Date"])

    # Identify the last date in the CSV file
    last_date = df["Date"].max()
    next_date = last_date + timedelta(days=1)

    # Define today's date
    today_date = datetime.today().date()

    # Check if the next date is in the past
    if next_date.date() < today_date:
        # Generate the Stooq URL for the missing data
        start_date_str = next_date.strftime("%Y%m%d")
        end_date_str = today_date.strftime("%Y%m%d")
        url = f'https://stooq.com/q/d/l/?s={stooq_ticker}&d1={start_date_str}&d2={end_date_str}&i=d'
        csv_file = f"{stooq_ticker}.csv"
        urlretrieve(url, csv_file)

        try:
            # Read the downloaded data
            new_data = pd.read_csv(csv_file)
            new_data.rename(columns={'Close': 'Value'}, inplace=True)

            # Append the new data to the DataFrame
            df = pd.concat([df, new_data], ignore_index=True)
            df["Date"] = pd.to_datetime(df["Date"])

            # Remove values of absolute 0 and sort values by date
            df = df[df["Value"] > 0]
            df.sort_values(by="Date", inplace=True)

            # Reset index and drop the old index column
            df.reset_index(drop=True, inplace=True)

        finally:
            # Remove the temporary CSV file
            os.remove(csv_file)

    # Export to CSV
    df.to_csv(local_csv_path, index=False)

    # Print the updated DataFrame
    print(df)

for asset in assets:
    local_csv_path = fr"/home/ruepa/FinancialData/Data/{asset.group}/{asset.name}.csv"  # Update with your path
    stooq_ticker = asset.stooq# Update with the Yahoo Finance ticker
    update_data_with_stooq(local_csv_path, stooq_ticker)