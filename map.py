from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import latitude as dict_1
import longitude as dict_2
import wind_speed as winds

# Define map.
m = Basemap(projection = 'merc', llcrnrlat = 0, urcrnrlat = 50,
			llcrnrlon = -90, urcrnrlon = -50, resolution = 'i')

# Write the basic structure for the map.
m.drawcoastlines(linewidth=0.1)
m.drawcountries(linewidth=0.1)
m.fillcontinents(color = 'grey', lake_color = 'black')

m.drawparallels(np.arange(13,50,10), color = 'grey', labels = 
				[False, True, False, False])
m.drawmeridians(np.arange(-90,-40,10), color = 'grey', labels =
				[False, False, False, True])
m.drawmapboundary(fill_color = 'black')

# Plot the title.
plt.title('Path Map of Hurricane Matthew')

# Set lat and lon variables to the refactored dictionary files.
lat = dict_1.latitudes
lon = dict_2.longitudes
ws = winds.wind_speeds

# Zip the three values above and make it into a list.
# And then zip them again.
# Zip function allows one variable to be taken out for examination.
# This is also the stage where one can perform statistical calculations.
a = list(zip(lon,lat,ws))
x,y,z = zip(*a)

# Convert lon and lat values into coordinates that can be mapped.
c1,c2 = m(x,y)

# Plot a line and then the coordinates.
m.plot(c1,c2, '-', color = 'yellow', linewidth = 1, zorder = 1)
m.scatter(c1,c2, c=z, marker='o', cmap="viridis", edgecolor="k", zorder = 2)

# Make the legend and the colour bar on the right.
plt.colorbar(label="wind speed")

plt.show()
