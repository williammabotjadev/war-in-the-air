import cartopy.crs as ccrs
import rasterio
import os

from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

from rasterio.plot import show

def process_img(filename, count, temp_path):
    # For convenience I have stored the COG file in the same directory as this notebook.
    # Note you may have given the file a different name.
    fp = filename

    raster = rasterio.open(fp)

    # This will print out the meta data associated with this file.
    print(raster.meta)

    # Tell the visualizer what is a 'no data' flag, in this case, 
    # from looking at the meta data above we see that it is -9999.0.
    NoData = raster.nodatavals

    # Data visualization units.
    unit = '[ mol / m-2 ]'

    # This is this title of the graph that will appear below.
    long_name = f"Tropospheric vertical column of carbon monoxide (CO) {count} \n\n {filename[47:]}"

    # We need to know the geopgrphical extent of the data, this is contained in the raster object.
    bbox = raster.bounds
    extent=[bbox[0],bbox[2],bbox[1],bbox[3]]
    print(bbox)

    # Here we set up the parameters needed to display the geographical data correctly.
    fig=plt.figure(figsize=(15, 12))

    # Here we set up a simple Plate Carree geographical projection.  This  handled by cartopy library.
    ax = plt.axes(projection=ccrs.PlateCarree())

    # The latest coastline data gets downloaded here, there may be a delay the first time you run this notebook.
    ax.coastlines(resolution='10m')
    ax.gridlines()
    ax.set_title(long_name, fontsize=16, pad=20.0, fontweight = 'bold')

    # Here we set the colour map for matplotlib. e.g. 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'jet'
    color = cm.gist_ncar

    color.set_bad('white')

    # In the norm setting below we normalise the data so that it scales between 0 to 1
    img = plt.imshow(raster.read(1), cmap = color,extent = extent,norm=LogNorm(),transform=ccrs.PlateCarree())

    cbar = fig.colorbar(img, ax=ax, orientation='horizontal', pad=0.1)
    cbar.set_label(unit, fontsize=16, fontweight = 'bold')
    cbar.ax.tick_params(labelsize=14)
    datef = datetime.now().strftime("%d-%m-%y%H:%M:%S")

    plt.savefig(f"./pre_images/{temp_path}/img{count}{datef}.png")

    # plt.show()

