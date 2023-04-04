from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
gas=pd.read_csv('gas_prices.csv')
print(gas)
plt.bar(gas.Year,gas.USA)
plt.title("Gas Prices in USA(in USD)")
plt.xlabel('Year')
plt.ylabel("US Dollars")
plt.show()
