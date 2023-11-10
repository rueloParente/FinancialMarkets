#Create list of financial assets that will link to Stooq for historical data
#Create python code to append to that data using yahoo finance
#Backup the CVS files every week to cloud
# Create a 2D array to store crypto names and their codes
assets = [
    ["Bitcoin", "BTC", "a", "a"],
    ["Ethereum", "ETH", "b", "b"],
    ["Litecoin", "LTC", "c", "c"],
    ["Cardano", "ADA", "d", "d"],
    # Add more cryptocurrencies as needed
]

# Accessing the elements in the 2D array
for crypto in assets:
    name, code, stooq, yahoo = crypto
    print(f"Name: {name}, Code: {code}, Name: {stooq}, Code: {yahoo}")