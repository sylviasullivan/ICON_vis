# run in conda environment ncplot
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

#from matplotlib.collections import LineCollection
#from matplotlib import cm
#import sys
#import xarray as xr
#import matplotlib.colors as colors
#from CloudSat_read import read_cloudsatcalipso_hdf_file


extent = [60, 100, -5, 40]
fig = plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.set_extent(extent)
ax.coastlines()
ll1 = np.asarray([[85,86,27,27],[85,86,28,28],[85,85,27,28],[86,86,27,28]])
ll2 = np.asarray([[85,86,13,13],[85,86,14,14],[85,85,13,14],[86,86,13,14]])
ll3 = np.asarray([[85,86,34,34],[85,86,35,35],[85,85,34,35],[86,86,34,35]])
for i in np.arange(4):
    ax.plot(ll1[i,:2],ll1[i,2:],transform=ccrs.Geodetic(),color='blue')
    ax.plot(ll2[i,:2],ll2[i,2:],transform=ccrs.Geodetic(),color='red')
    ax.plot(ll3[i,:2],ll3[i,2:],transform=ccrs.Geodetic(),color='green')
fig.savefig('../output/trajectory_boxes.png',bbox_inches='tight',dpi=100)
plt.show(block=True)
