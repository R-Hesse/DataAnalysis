# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:02:36 2022

@author: hesse

"""

# TRADE CLASS TO STORE USER TRADES

class Trade:
   def __init__(self, ticker, buyDate, sellDate, buy, sell):
     self.ticker = ticker
     self.buyDate = buyDate
     self.sellDate = sellDate
     self.buy = buy
     self.sell = sell
     
    
   
   def getTrade(self):
       return self
   
   def getTicker(self):
        return self.ticker
      
   def getBuyDate(self):
       return self.buyDate
      
   def getSellDate(self):
       return self.sellDate
      
   def getBuy(self):
       return self.buy
      
   def getSell(self):
       return self.sell
      
   