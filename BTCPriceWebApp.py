#Grant Slattery
#9/4/20
#Source of project: https://dash.plotly.com/datatable
#API & data Powered by CoinDesk: https://www.coindesk.com/price/bitcoin
#Scraping data and displaying it on the web using dash, 
#panda, requests, and more with Python

import dash
import dash_table
import pandas as pd
import requests


#############
#Scrape data#
#############

#Scraping with requests
bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
#Addition work for requests
response = requests.get(bitcoin_api_url)
response_json = response.json()


#################
#Refine raw data#
#################

#First round of raw data cleaning
priceData = response_json.get("bpi")

#Create Dash Table Data Frame with priceData variable
newpdFrame = pd.DataFrame(data=priceData)


#########################
#Display data on the web#
#########################

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns = [{"name": i, "id": i} for i in newpdFrame.columns],
    data = newpdFrame.to_dict('records'),
)

print("Program running")

if __name__ == '__main__':
    app.run_server(debug=True)
