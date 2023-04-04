from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
gas=pd.read_csv('gas_prices.csv')
print(gas)
#plt.plot(gas.Year,gas.USA,'b.-',label="USA")
#plt.plot(gas.Year,gas.Canada,'r.-',label="Canada")
#plt.plot(gas['Year'],gas['South Korea'],'g.-',label="South Korea")
for country in gas:
    if country != 'Year':
       plt.plot(gas.Year,gas[country],marker='.',label=country)

plt.title("Gas Prices over Time(in USD)")
plt.xlabel('Year')
plt.ylabel("US Dollars")
plt.xticks(gas.Year[::3])
plt.legend()
plt.show()
