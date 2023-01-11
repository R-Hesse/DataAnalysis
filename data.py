# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:04:53 2022

@author: hesse
"""

# DATA CLASS TO STORE API DATA

class Data:
   def __init__(self, ticker, date, dailyOpen, dailyHigh, dailyLow, dailyClose, dailyVolume):
     self.ticker = ticker
     self.date = date
     self.dailyOpen = dailyOpen
     self.dailyHigh = dailyHigh
     self.dailyLow = dailyLow
     self.dailyClose = dailyClose
     self.dailyVolume = dailyVolume
   
   def getData(self):
       return self
   
   def getTicker(self):
        return self.ticker
      
   def getDate(self):
       return self.date
      
   def getOpen(self):
       return self.dailyOpen
      
   def getHigh(self):
       return self.dailyHigh
      
   def getLow(self):
       return self.dailyLow
      
   def getClose(self):
       return self.dailyClose
      
   def getVolume(self):
       return self.dailyVolume
