import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'R7SX528FT8JX6F7O'
ts = TimeSeries(key =api_key, output_format = 'pandas')
data, meta_data = ts.get_intraday(symbol = 'MSFT', interval = '1min', outputsize = 'full')
data.
print(data)

i = 1
while i ==1 :
    data.to_excel("stock_quote.xlsx")
    time.sleep(60)
