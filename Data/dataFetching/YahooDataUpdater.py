import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from Data.dataFetching.Assets import assets


def update_data_with_yahoo_finance(local_csv_path, yahoo_ticker):
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
        # Fetch data up to today
        new_data = \
        yf.download(tickers=yahoo_ticker, start=next_date.strftime("%Y-%m-%d"), end=today_date.strftime("%Y-%m-%d"))[
            "Close"]

        # Append the new data to the DataFrame
        new_data = new_data.reset_index()
        new_data.rename(columns={'Close': 'Value', 'index': 'Date'}, inplace=True)
        df = pd.concat([df, new_data], ignore_index=True)

    # Remove values of absolute 0
    df = df[df["Value"] > 0]

    # Sort values by date
    df.sort_values(by="Date", inplace=True)

    # Reset index and drop the old index column
    df.reset_index(drop=True, inplace=True)

    # Export to CSV
    df.to_csv(local_csv_path, index=False)

    # Print the updated DataFrame
    print(df)


# Example usage
for asset in assets:
    local_csv_path = fr"/home/ruepa/FinancialData/Data/{asset.group}/{asset.name}.csv"  # Update with your path
    yahoo_ticker = asset.yahoo  # Update with the Yahoo Finance ticker
    update_data_with_yahoo_finance(local_csv_path, yahoo_ticker)