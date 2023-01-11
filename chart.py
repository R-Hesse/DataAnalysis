# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:31:55 2022

@author: hesse
"""


from ta.trend import MACD
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import pandas as pd




# METHOD TO BUID MY CHART 

def getChart():
    
    # RENDERS CHART IN BROWSER OR IDE
    
    pio.renderers.default='browser'
    #pio.renderers.default='svg'
    


    # OPENS DATA FILE FROM API FILE 
    # ** WARNING - YOU'LL NEED TO CHANGE FILE LOCATION TO SUIT YOUR SYSTEM**
    
    file = open('C:/Users/hesse/PythonTradingBot/data.csv')

    type(file)

    df = pd.read_csv(file)
    
    
    
    # METHOD TO ISOLATE THE TICKER SYMBOL FOR CHART TITLE
    
    ticker = df['Ticker'].values.tolist()
    i = 0
        
    for x in ticker:
        
    # SETS COMPANY NAME
       company = ticker[0]
    
    # TEST SCRIPT TO ENSURE PROPER STOCK IS CALLED
    print("Ticker Symbol")
    print(company + "\n")
        
    
    
    
    # MACD LINE IS ACCURATE FOR THE FIRST 75% OF THE CHART BUT FAILS TO SPAN 
    # THE WHOLE WAY ACROSS. MANY DIFFERENT ECUATIONS WERE TRIED, BUT THE 
    # TA.TRENT MACD IMPORT WAS THE CLOSEST I COULD GET TO AN ACCURATE INDICATOR
    
    macd = MACD(close=df['Close'], 
            window_slow=26,
            window_fast=12, 
            window_sign=9)
    df['MACD'] = MACD(close=df['Close'],window_slow=26,window_fast=12, window_sign=9)
    
    
    # TEST SCRIPT CHECKING THE MACD DATAFRAME
    print("CURRENT DATAFRAME HOLDING MACD OBJECT INSTANCES")
    print(df["MACD"])
    print("")


   
    # RSI LINE IS 90% ACCURATE. 15 MOCK VALUES WERE ADDED TO KEEP THE
    # INDICATOR FROM BOTTOMING OUT AT THE END. THESE MOCK VALUES ARE FOR   
    # COSMETIC DETAILS AND WILL NOT CURRENTLY BE USED FOR TRADING.
   
    # GET ALL CLOSE PRICES
    prices = df['Close'].values.tolist()
 
    i = 0
    
    # USED FOR DAILY PRICE DIRECTION
    upPrices=[]
    downPrices=[]

    # TEST SCRIPT CHECKING DATA INPUT AND RSI DATAFRAME
    print("CURRENT DATAFRAME HOLDING CLOSING PRICES FOR RSI")
    print(prices)
    print("")

    
    for x in prices:
        
        # GETS TWO LIST INSTANCES OF CLOSING PRICE
        one = prices[i]
        two = prices[i-1]
        
        
        # SETS DAILY PRICE DIRECTION
        if i == 0:
            upPrices.append(0)
            downPrices.append(0)
        else:
            if (one-two)>0:
                upPrices.append(one-two)
                downPrices.append(0)
            else:
                downPrices.append(one-two)
                upPrices.append(0)
        
        x += 1 
        i += 1
        
    x = 0
    
    # LOOP TO CALCULATE DAILY AVERAGE GAIN OR LOSS
    avg_gain = []
    avg_loss = []

    
    while x < len(upPrices):
        if x <15:
            avg_gain.append(0)
            avg_loss.append(0)
        else:
            sumGain = 0
            sumLoss = 0
            y = x-14
            while y<=x:
                sumGain += upPrices[y]
                sumLoss += downPrices[y]
                y += 1
            avg_gain.append(sumGain/14)
            avg_loss.append(abs(sumLoss/14))
        x += 1
    p = 0
    RS = []
    RSI = []
    
    # MOCK DATA TO FILL THE 15 EMPTY ROWS DUE TO THE NATURE OF THE EQUATION
    # EXTRA DATA IS NEEDED TO POPULATE THE WHOLE CHART AND THIS API CHARGES
    # FEES TO PULL MORE DATA THEN THIS BOT IS CURRENTLY RECIEVING! 
    
    mockRSI =0.72023453234

    i = 0
    
    # LOOP CALCULATING THE RELATIVE STRENGTH AND THE RELATIVE STRENGTH INDEX
    
    while p < len(prices):
        
        if p <15:
            
            # 15 MOCK VALUES TO FILL OUT CHART
            RSvalue = (mockRSI)
            RS.append(RSvalue)
            RSI.append(100 - (100/(1+RSvalue)))
            mockRSI += 0.04420
        else:
            # REMAINING REAL VALUES
            RSvalue = (avg_gain[p]/avg_loss[p])
            RS.append(RSvalue)
            RSI.append(100 - (100/(1+RSvalue)))
        p+=1
   
    # SETS THE RSI DATAFRAME 
    
    df["RSI"] = RSI
    

    # TEST SCRIPT TO VIEW THE RSI LIST WHICH HELPS TEST THE SCRIPS ACCURACY 
    # RUNNING THE ABOVE  EQUATION: RSI = (100 - (100/(1+RS)))
    
    print("RSI LIST")
    print(RSI)
    print("")
    


        
    # 13/38 DAY MOVING AVERAGE LINES AND THE EXPONENTIAL MOVING AVERAGE (EMA)
    
    # GET PRICES AND SET WINDOWS FOR EQUATION
    prices = df['Close'].values.tolist()
    thirteen = 13
    fortyEight = 48
    i = 0
    
    # LISTS TO HOLD AVERAGES
    moving_averages_13 = []
    moving_averages_48 = []

    # LOOP THROUGH ARRAY WITH 13 INSTANCES
    while i < len(prices) - thirteen + 1:
        
        # CURRENT WINDOW
        window = prices[i : i + thirteen]
        
        # AVERAGE OF CURRENT WINDOW
        window_average = round(sum(window) / thirteen, 2)
        
        # APPEND TO 13 DAY MOVING AVERAGE LIST
        moving_averages_13.append(window_average)
        
        # SHIFT WINDOW BY 1
        i += 1
    
    
    # LOOP THROUGH ARRAY WITH 48 INSTANCES
    i = 0
    while i < len(prices) - fortyEight + 1:
        
        # CURRENT WINDOW
        window = prices[i : i + fortyEight]
        
        # AVERAGE OF CURRENT WINDOW
        window_average = round(sum(window) / fortyEight, 2)
        
        # APPEND TO 48 DAY MOVING AVERAGE LIST
        moving_averages_48.append(window_average)
        
        # SHIFT WINDOW BY 1
        i += 1
        
        
    # EMA IMPORTED EQUATION
    
    df['EMA'] = df['Close'].expanding().mean()

    emaList = df['EMA'].values.tolist()
    
  
    # TEST SCRIPT TO VIEW THE 13/48 MA AND OVERALL EMA
    print("13MA")
    print(moving_averages_13)
    print("")

    print("48MA")
    print(moving_averages_48)
    print("")

    print("EMA")
    print(emaList)
    print("")
  
    
    
    
    # FIGURE TO GENERATE CHARTS, LINES, AND (SOON TO BE) ALERTS 

    fig = make_subplots(rows=4, cols=1, shared_xaxes=True,
                    vertical_spacing=0.01, 
                    row_heights=[0.5,0.1,0.2,0.2])
    
    # CANDLESTICK CHART
    
    fig.add_trace(go.Candlestick(x=df['Date'],
                          open=df['Open'],
                          high=df['High'],
                          low=df['Low'],
                          close=df['Close'],
                          name='Price Movement'), row=1, col=1)
 
    
    # 13 DAY MOVING AVERAGE
    
    fig.add_trace(go.Scatter(x=df['Date'], 
                         y=moving_averages_13, 
                         opacity=0.7, 
                         line=dict(color='green', width=2), 
                         name='13 MA'))
    
    # 48 DAY MOVING AVERAGE
    
    fig.add_trace(go.Scatter(x=df['Date'], 
                         y=moving_averages_48, 
                         opacity=0.7, 
                         line=dict(color='red', width=2), 
                         name='48 MA'))
    
    # EXPONENTIAL MOVING AVERAGE

    fig.add_trace(go.Scatter(x=df['Date'], 
                         y=df['EMA'], 
                         opacity=0.7, 
                         line=dict(color='white', width=2), 
                         name='Exponential Moving Average'))
    
    
    # VOLUME CHART 
    
    colors = ['green' if row['Open'] - row['Close'] >= 0 
          else 'red' for index, row in df.iterrows()]
    fig.add_trace(go.Bar(x=df['Date'], 
                     y=df['Volume'],
                     marker_color=colors,
                     name='Volume'
                    ), row=2, col=1)
    

    
    # RSI CHART 
    
    fig.add_trace(go.Scatter(x=df['Date'],
                         y=df["RSI"],
                         line=dict(color='blue', width=2),
                         name='RSI'
                        ), row=3, col=1)
   
    
    # MACD CHART
    
    
    colors = ['green' if val >= 0 
          else 'red' for val in macd.macd_diff()]
    fig.add_trace(go.Bar(x=df['Date'], 
                      y=macd.macd_diff(),
                      marker_color=colors,
                      name='MACD'
                    ), row=4, col=1)
    
    
    # LAYOUT AND GRID SETTINGS

    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgb(128,128,128)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(128,128,128)')
    fig.update_layout(title=('Ryan\'s Crossover: ' + company), title_x=0.5, plot_bgcolor='rgb(0,0,0)', paper_bgcolor='rgb(0,0,0)', font_color="white")
    fig.update_layout(xaxis_rangeslider_visible=False, xaxis_rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=["2022-06-20", "2022-07-04", "2022-09-05", "2022-11-24", "2022-12-26"])])
    
    

    # CHART TITLES

    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)
    fig.update_yaxes(title_text="RSI", showgrid=False, row=3, col=1)
    fig.update_yaxes(title_text="MACD", showgrid=False, row=4, col=1)
    
    # SHOW CHART
    
    fig.show() 