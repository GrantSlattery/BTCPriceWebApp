#Grant Slattery
#9/4/20
#Source of project: https://dash.plotly.com/datatable
#API & data Powered by CoinDesk: https://www.coindesk.com/price/bitcoin
#Scraping data and displaying it on the web using dash, 
#panda, requests, and morenwith Python

import dash
import dash_table
import pandas as pd
import requests
import datetime



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
timeStamp = response_json.get("time")
coindeskDisclaimer = response_json.get("disclaimer")
priceData = response_json.get("bpi")

#Final price related data cleaning
usdData = priceData.get("USD")
gbpData = priceData.get("GBP")
eurData = priceData.get("EUR")

usdBtcPrice = usdData.get("rate")
gbpBtcPrice = gbpData.get("rate")
eurBtcPrice = eurData.get("rate")

#Final time related data cleaning
time1 = timeStamp.get("updated")
time2 = timeStamp.get("updatedISO")
time3 = timeStamp.get("updateduk")


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