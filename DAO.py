import sqlite3
from sqlite3 import Error
from random import randrange
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


buyDate=[]
sellDate=[]
buy=[]
sell=[]
GL=[]



def trade():
    
    conn = None
    try:
        conn = sqlite3.connect('trade.db')
    except Error as e:
        print(e)
        
    # CREATES TRADES TABLE IN DB 
    
    #conn.execute('''DROP TABLE TRADES;''');
    conn.execute('''CREATE TABLE IF NOT EXISTS TRADES
                     (ID INT PRIMARY KEY     NOT NULL,
                      TICKER           TEXT    NOT NULL,
                      BUYDATE           TEXT    NOT NULL,
                      SELLDATE           TEXT    NOT NULL,
                     BUY            TEXT     NOT NULL,
                     SELL           TEXT     NOT NULL);''');

    
    #SELECT ALL FROM TABLE FOR CHART
    cursor = conn.execute("SELECT ID, TICKER, BUYDATE, SELLDATE, BUY, SELL from TRADES")
    
    for row in cursor:
        
        # TEST SCRIPTS TO VIEW ALL DATABASE INFO 
        
        print("ID = ", row[0])
        print("TICKER = ", row[1])
        print("BUYDATE = ", row[2])
        print("SELLDATE = ", row[4])
        print("BUY = ", row[3])
        print("SELL = ", row[5])    
        
        buyDate.append(row[2])
        sellDate.append(row[3])
        buy.append(row[4])
        sell.append(row[5])
        
        sold = float(row[5])
        bought = float(row[3])
        
        # APPEND THE GAIN OR LOSS FOR EACH TRADE
        
        GL.append(sold-bought)
        
        
    # USER LOGGS TRADE WITH SYSTEM
    print("\nPLEASE LOG ANY TRADES WITH OUR SYSTEM HERE\n")
        
    # TRADE INSTANCE DETAILS
    tradeId = randrange(500)
    tic = input("Purchased Ticker: ")
    puda = input("Purchased Date (2022-12-31): ")
    bu = input("Purchase Price: ")
    puse = input("Date Sold (2022-12-31): ")
    se = input("Price Sold: ")
        
    sql = ''' INSERT INTO TRADES(ID,TICKER,BUYDATE,SELLDATE,BUY,SELL)
              VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, (tradeId, tic, puda, bu, puse, se))
    conn.commit()
    getTrade()
    
def getTrade():
    # RENDERS A NEW BROWSER WITH THE USER'S TRADE GAINS/LOSSES
    pio.renderers.default='browser'

    file = open('C:/Users/hesse/DexBot/data.csv')

    type(file)

    df = pd.read_csv(file)
   
    
    fig = go.Figure()

    #SCATTERPLOT OF THE GAIN/LOSS RECORDED ON THE SALE DATE
    fig.add_trace(go.Scatter(
    x=df['Date'],
    y=GL
    ))

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgb(128,128,128)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(128,128,128)')
    fig.update_layout(title=('Profit/Loss Details'), title_x=0.5, plot_bgcolor='rgb(0,0,0)', paper_bgcolor='rgb(0,0,0)', font_color="white")
    fig.update_layout(xaxis_rangeslider_visible=False)

    fig.show()
        
    

    
    
    