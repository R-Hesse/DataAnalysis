# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:56:16 2022

@author: hesse
"""

import tkinter as tk
from tkinter import simpledialog


# GUI TO GET REQUESTED STOCK

def getStock():
   
    root = tk.Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.overrideredirect(1)
    root.withdraw()
    root.update_idletasks()

    
    ticker = simpledialog.askstring(title="DexBot",
                                      prompt="Please Enter A Valid NYSE Ticker Symbol", parent=root)
    

    return ticker


# GUI TO GET REQUESTED TIMEFRAME (ONLY DAILY WORKS CURRENTLY)

def getTime():
    
    root = tk.Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.overrideredirect(1)
    root.withdraw()
    root.update_idletasks()
    
    timeframe = simpledialog.askstring(title="DexBot",
                                      prompt="Please Enter a Chart Time Interval (1, 5, 15, 30, 60, Daily)")

    return timeframe


# GUI TO LOG TRADE TO DATABASE *IN DEVELOPMENT*

def getTrade():
    
    root = tk.Tk()
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.overrideredirect(1)
    root.withdraw()
    root.update_idletasks()
    
    stock = simpledialog.askstring(title="DexBot",
                                      prompt="Please Enter Ticker of A Purchase or Sale")
    
    buyOpen = simpledialog.askstring(title="DexBot",
                                      prompt="Please Enter A Buy Amount")
    
    sellClose = simpledialog.askstring(title="DexBot",
                                      prompt="Please Enter A Sell Amount")
    
    return stock, buyOpen, sellClose
    
    

    

