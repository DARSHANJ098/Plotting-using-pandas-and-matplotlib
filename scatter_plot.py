from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
gas=pd.read_csv('gas_prices.csv') #reading a csv file using pandas
print(gas)
for country in gas:
    if country != 'Year':
         plt.scatter(gas.Year,gas[country],label=country)
plt.legend() # adds the icons of countries at the top
plt.title("Scatter plot of Gas Prices(in USD)")
plt.xlabel("Year")
plt.ylabel("US Dollars")
plt.show()         
