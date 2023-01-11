# DataAnalysis

This repository contains a version of my Python stock trading algorithm that is currently still under development. The system calls API data and parses it using JSON where the received data is then cleansed, written to a temp file, and used to populate a chart using Plotly and Pandas. This generates a visualized stock chart containing all the data necessary to make the suggested trades.

The user must adhere to the trading plan as follows: If the 13 MA crosses above the 48 MA while volume is increasing, MACD is in the green, and the RSI is above 50, the user should buy the security. If the 13 MA crosses below the 48 MA while the volume is decreasing, MACD is in the red, and the RSI is below 50, the user should sell a security. After the user logs a trade in the database a chart populates with the previous trades gain/loss points on a scatterplot
