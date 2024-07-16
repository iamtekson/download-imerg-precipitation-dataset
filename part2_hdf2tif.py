from osgeo import gdal, os, osr
from qgis.core import *
import qgis.utils


os.chdir(r"D:\projects\mrg_data_download\HDF5")

#print(os.listdir(os.getcwd()))

totallinks = os.listdir(os.getcwd())

hdflinks = []
for link in totallinks:
    if link[-4:] == 'HDF5':
        hdflinks.append(link)

for link in hdflinks:
    if link[-4:] == 'HDF5':
        print(link)
        hdf_ds = gdal.Open(link, gdal.GA_ReadOnly)

        band_ds = gdal.Open(hdf_ds.GetSubDatasets()[7][0], gdal.GA_ReadOnly) #choose the 5th dataset that corresponds to precipitationCal
        x = band_ds.RasterXSize
        y = band_ds.RasterYSize
        out_band = 1
        
        print(x,y)
        
        band_array = band_ds.ReadAsArray()
  
        band_array[band_array<0] = 0 #filter all NaN values that appear as negative values, specially for the tiff representation

        geotransform = ([-180,0.1,0,90,0,-0.1])

        raster = gdal.GetDriverByName('GTiff').Create("../Tiff/"+link[:-5]+".tif",y,x,out_band,gdal.GDT_Float32)

        raster.SetGeoTransform(geotransform)

        srs=osr.SpatialReference()
        srs.ImportFromEPSG(4326)
        raster.SetProjection(srs.ExportToWkt())
        raster.GetRasterBand(1).WriteArray(band_array.T[::-1])
        
        raster = None
