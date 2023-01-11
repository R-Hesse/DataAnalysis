# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 07:30:34 2022

@author: hesse

API KEY: 5PZBSPYLFWQGIU1C

"""


import requests
from data import Data
from chart import getChart
from datetime import date, timedelta
import time
import json
import DAO as db
from csv import DictWriter
import os


# CREATE DATA FILE

filePath = 'C:/Users/hesse/PythonTradingBot/data.csv'

file = 'data.csv'

if (os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)
  print("file deleted")
else:
  print("file not found")


# CALL GUI FOR USER INPUT
ticker = input("Please Enter A Valid NYSE Ticker Symbol: ")
timeframe = input("Please Enter a Chart Time Interval (1, 5, 15, 30, 60, Daily): ")

# DATABASE LOGGING METHOD IN DEVELOPMENT
# db = getTrade()


# API COLLECTION WITH DIFFERENT TIMEFRAMES
# CURRENTLY ONLY THE DAILY TIMEFRAME CAN POPULATE A CHART

daily_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&apikey=5PZBSPYLFWQGIU1C'

one_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=5PZBSPYLFWQGIU1C'

five_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=5min&apikey=5PZBSPYLFWQGIU1C'

fifteen_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=15min&apikey=5PZBSPYLFWQGIU1C'

thirty_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=30min&apikey=5PZBSPYLFWQGIU1C'

sixty_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=60min&apikey=5PZBSPYLFWQGIU1C'


# Multiple Timeframes
#PROVED TO BE TOO MUCH WORK TO INCORPERATE 

# if timeframe == "1":
#    daily = requests.get(one_api)
# elif timeframe == "5":
#     daily = requests.get(five_api)
# elif timeframe == "15":
#     daily = requests.get(fifteen_api)
# elif timeframe == "30":
#     daily = requests.get(thirty_api)
# elif timeframe == "60":
#     daily = requests.get(sixty_api)
# elif timeframe == "Daily":
#     daily = requests.get(daily_api)
# else:
#     print("ERROR: Please Enter a Valid Time ")


# CALLS THE DAILY API AND PARSES THE JSON DATA

daily = requests.get(daily_api)

data = daily.text

parse_data = json.loads(data)

#DATE IS USED FOR CHARTING

dateToday = date.today()

date = dateToday.strftime("20%y-%m-%d")


# POPULATED DATA FILE MANAGMENT 

fileExists = os.path.isfile(filePath)

headers = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']


with open (filePath, 'a') as csvfile:
    
    writer = DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

    if not fileExists:
        writer.writeheader()  # file doesn't exist yet, write a header
        

# POPULATES DATA FILE WITH API DATA WITH FOR LOOP

for x in range(1,145):
    print()

    # Accounts for Dates the NYSE is Closed
    if date == "2023-01-11" or date == "2023-01-07" or date == "2023-01-02" or date == "2023-01-01" or date == "2023-01-08" or date == "2022-07-25" or date == "2022-12-14" or date =="2022-06-14" or date == "2022-12-31" or date == "2022-12-25" or date == "2022-12-24" or date == "2022-12-18" or date == "2022-12-17" or date == "2022-12-11" or date == "2022-12-10" or date == "2022-12-04" or date == "2022-12-03" or date == "2022-11-27" or date == "2022-11-26" or date == "2022-11-20" or date == "2022-11-19" or date == "2022-11-13" or date == "2022-11-12" or date == "2022-11-06" or date == "2022-11-05" or date == "2022-10-30" or date == "2022-10-29" or date == "2022-10-23" or date == "2022-10-22" or date == "2022-10-16" or date == "2022-10-15" or date == "2022-10-09" or date == "2022-10-08" or date == "2022-10-02" or date == "2022-10-01" or date == "2022-09-25" or date == "2022-09-24" or date == "2022-09-18" or date == "2022-09-17" or date == "2022-09-11" or date == "2022-09-10" or date == "2022-09-04" or date == "2022-09-03" or date == "2022-08-28" or date == "2022-08-27" or date == "2022-08-21" or date == "2022-08-20" or date == "2022-08-14" or date == "2022-08-13" or date == "2022-08-07" or date == "2022-08-06" or date == "2022-07-31" or date == "2022-07-30" or date == "2022-07-24" or date == "2022-07-23" or date == "2022-07-17" or date == "2022-07-16" or date == "2022-07-10" or date == "2022-07-09" or date == "2022-07-03" or date == "2022-07-02" or date == "2022-06-26" or date == "2022-06-25" or date == "2022-06-19" or date == "2022-06-18" or date == "2022-06-12" or date == "2022-06-11" or date == "2022-06-05" or date == "2022-06-04" or date == "2022-06-20" or date == "2022-07-04" or date == "2022-09-05" or date == "2022-11-24" or date == "2022-12-26":
        newDate = dateToday - timedelta(days=x)
        date = newDate.strftime("20%y-%m-%d")
        continue
    
    # API Pulls Data From Source
    # Multiple Timeframes Under Development! 
    if timeframe == "1":
        
        print("ERROR: Please Enter a Valid Time ")
        break
        
        # MOCK CODE FOR WHEN BUG IS FIXED 
        
        # full = parse_data['Time Series (1min)']
        # dailyOpen = parse_data['Time Series (1min)'][date]['1. open']
        # dailyHigh = parse_data['Time Series (1min)'][date]['2. high']
        # dailyLow = parse_data['Time Series (1min)'][date]['3. low']
        # dailyClose = parse_data['Time Series (1min)'][date]['4. close']
        # dailyVolume = parse_data['Time Series (1min)'][date]['5. volume']
       
    elif timeframe == "5":
        print("ERROR: Please Enter a Valid Time ")
        break
                
    elif timeframe == "15":
        print("ERROR: Please Enter a Valid Time ")
        break
        
    elif timeframe == "30":
        print("ERROR: Please Enter a Valid Time ")
        break
        
    elif timeframe == "60":
                
        print("ERROR: Please Enter a Valid Time ")
        break
        
    elif timeframe == "Daily":
        
        # DAILY TIMEFRAME DATA PARSE 
        
        full = parse_data['Time Series (Daily)']
        dailyOpen = parse_data['Time Series (Daily)'][date]['1. open']
        dailyHigh = parse_data['Time Series (Daily)'][date]['2. high']
        dailyLow = parse_data['Time Series (Daily)'][date]['3. low']
        dailyClose = parse_data['Time Series (Daily)'][date]['4. close']
        dailyVolume = parse_data['Time Series (Daily)'][date]['6. volume']    
        
    else:
        print("ERROR: Please Enter a Valid Time ")
        break

    # DATA CLASS AND DAILY DATA DICTIONARY POPULATED 
    
    data = Data(ticker, date, dailyOpen, dailyHigh, dailyLow, dailyClose, dailyVolume)
    
    dailyData = {"Ticker" : ticker, "Date" : data.getDate(), "Open" : data.getOpen(), "High" : data.getHigh(), "Low" : data.getLow(), "Close" : data.getClose(), "Volume" : data.getVolume()}

    # WRITES API DAILY DATA TO DATA FILE FOR CHART CLASS
    
    with open('data.csv', 'a') as dataFile:
        
        dicOject = DictWriter(dataFile, fieldnames=headers)
        dicOject.writerow(dailyData)
        dataFile.close()
    
    # SETS/FORMATS NEW DATE FOR LOOP ITERATION
    
    newDate = dateToday - timedelta(days=x)
    
    date = newDate.strftime("20%y-%m-%d")
 
    # TEST SCRIPTS TO PRINT VALUES FOR COMPARISON  
    
    print("Ticker: " + ticker)
    print("Date: " + data.getDate())
    print("Open: " + data.getOpen())
    print("High: " + data.getHigh())
    print("Low: " + data.getLow())
    print("Close: " + data.getClose())
    print("Volume: " + data.getVolume())


# CALLS ALL METHODS
getChart()
time.sleep(5)
db.trade()

    

    
