import pandas as pd
import matplotlib.pyplot as plt

## Reading AE51
ae51_pth = 'data_FabForno/AE51_forno_surface.dat'
ae51 = pd.read_csv(ae51_pth, skiprows=14, sep = ';')
ae51['datetime'] = pd.to_datetime(ae51.Date + ' ' + ae51.Time)
ae51 = ae51[['datetime','BC']]


## Reading Airnote
airnote_pth = 'data_FabForno/Airnote_forno.csv'
airnote = pd.read_csv(airnote_pth)
airnote['datetime'] = pd.to_datetime(airnote[['Year','Month','Day','Hour','Minute']])
airnote = airnote.loc[:,['datetime','PM1','PM2.5','PM10']]

print(ae51)
print(airnote)

# ## Plotting
# fig, ax = plt.subplots()
# ax.plot(ae51.datetime, ae51.BC, c = 'red')
# ax2 = ax.twinx()
# ax2.plot(airnote.datetime, airnote.PM10, c = 'k')
# plt.show()


# ## Mean of 30 minutes
ae51.set_index('datetime', inplace = True)
ae51 = ae51['BC'].resample('30Min').mean().to_frame()

airnote.set_index('datetime', inplace = True)
airnote = airnote[['PM1','PM2.5','PM10']].resample('30Min').mean()

print(ae51)
print(airnote)

# ## Merging
m = ae51.merge(airnote, 'inner', 'datetime')
m.reset_index(inplace=True)
print(m)

# ## Plotting the relationship
plt.figure()
plt.scatter(m.PM10, m.BC)

plt.show()