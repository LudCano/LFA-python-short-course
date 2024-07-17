import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pth = 'data_FabForno/es203_20230726.csv'

radio = pd.read_csv(pth, skiprows=15)
radio['datetime'] = pd.to_datetime(radio['date [d-m-y GMT]'] + radio[' time [h:m:s GMT]'])
#print(radio.columns)
temp = radio[' iMet air temperature (corrected) [deg C]']
print(temp)

plt.figure()
plt.plot(temp)
plt.show()


### SMOOTHING VIA RUNNING OR MOVING AVERAGE
# n is the step after and before the central value
n = 20
# the number of values of the new vector would be
k = len(temp) - 2*n
# creating an empty array
new = np.zeros(k)
# averaging over the groups
for idx, val in enumerate(new):
    idx = idx + n
    grp = temp[idx - n: idx + n + 1]
    mn = np.mean(grp)
    new[idx-n] = mn

plt.figure()
plt.plot(temp)
plt.plot(new)
plt.show()


## MAKING A ROLLING WINDOW WITH PANDAS

# radio2 = radio.copy()
# radio2.set_index('datetime', inplace=True)
# temp2 = radio2[' iMet air temperature (corrected) [deg C]']
# rol = temp2.rolling('20s').mean().to_list()

# plt.figure()
# plt.plot(temp)
# plt.plot(rol)
# plt.plot(new)
# plt.show()
