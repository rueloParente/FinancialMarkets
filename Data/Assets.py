# This file contains the Crypto class which is used to store the name, code, Stooq code and Yahoo code for each crypto
class Assets:
    def __init__(self,group, name, code, stooq, yahoo):
        self.group = group
        self.name = name
        self.code = code
        self.stooq = stooq
        self.yahoo = yahoo

    def __str__(self):
        return f"Group:{self.group} Name: {self.name}, Code: {self.code}, Stooq Code: {self.stooq}, Yahoo Code: {self.yahoo}"

# Example of how to use the class with actual codes for Stooq and Yahoo
assets = [
    #Crypto
    Assets("Crypto", "Bitcoin", "BTC", "BTCUSD", "BITCOIN"),
    Assets("Crypto","Ethereum", "ETH", "ETH.V", "ETHEREUM"),
    #Assets("Crypto","Cardano", "ADA", "ADA.V", "CARDANO"),
    #Stocks
    Assets("Stocks","Crispr", "CRSP", "CRSP.US", "CRSP"),
    Assets("Stocks","Salesforce", "CRM", "CRM.US", "CRM"),
    #Assets("Stocks","Intel", "INTC", "INTC.US", "INTC"),
    #Assets("Stocks","Block", "SQ", "SQ.US", "SQ"),
    #Assets("Stocks","Nvidia", "NVDA", "NVDA.US", "NVDA"),
    #Assets("Stocks","Shopify", "SHOP", "SHOP.US", "SHOP"),
    #Indexes
    Assets("Index","Nasdaq", "NDX", "^NDX", "NDX"),
    Assets("Index","S&P500", "SPX", "^SPX", "SPX"),
    #Assets("Indexes","Dow Jones", "DJI", "^DJI", "DJI"),
    #Metals
    Assets("Metals","Gold", "XAU", "XAUUSD", "XAU"),
    Assets("Metals","Silver", "XAG", "XAGUSD", "XAG"),
    #Forex
    Assets("Forex","EURUSD", "EURUSD", "EURUSD", "EURUSD"),
    Assets("Forex","GBPUSD", "GBPUSD", "GBPUSD", "GBPUSD"),
]