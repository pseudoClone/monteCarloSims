import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

from pandas_datareader import data as pdr

# Import data

def get_data(stocks, start, end): #end data and start date
    stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData['Close']
    returns = stockData.pct_change() # Daily changes
    meanReturns = returns.mean() # Compute the main return
    covMatrix = returns.cov() # Returns the covariance matrix
    return meanReturns, covMatrix

stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stock = [stock + '.AX' for stock in stockList]

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 300)


meanReturns, covMatrix = get_data(stocks, startDate, endDate)

print(meanReturns)
