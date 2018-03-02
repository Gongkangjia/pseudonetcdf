__all__ = ['test_cloud_rain_Memmap', 
           'test_height_pressure_Memmap', 
           'test_height_pressure_Read', 
           'test_humidity_Memmap', 
           'test_humidity_Read', 
           'test_ipr_Memmap', 
           'test_ipr_Read', 
           'test_irr_Read', 
           'test_irr_Memmap', 
           'test_landuse_Memmap', 
           'test_lateral_boundary_Memmap', 
           'test_one3d_Memmap', 
           'test_one3d_Read', 
           'test_point_source_Memmap', 
           'test_point_source_Read', 
           'test_temperature_Memmap', 
           'test_temperature_Read', 
           'test_uamiv_Memmap', 
           'test_uamiv_Read', 
           'test_uamiv_Write', 
           'test_vertical_diffusivity_Memmap', 
           'test_vertical_diffusivity_Read', 
           'test_wind_Memmap', 
           'test_wind_Read']


from PseudoNetCDF.camxfiles.cloud_rain.Memmap import TestMemmap as test_cloud_rain_Memmap
# from PseudoNetCDF.camxfiles.finst.Memmap import TestMemmap as test_finst_Memmap
from PseudoNetCDF.camxfiles.height_pressure.Memmap import TestMemmap as test_height_pressure_Memmap
from PseudoNetCDF.camxfiles.height_pressure.Read import TestRead as test_height_pressure_Read
from PseudoNetCDF.camxfiles.humidity.Memmap import TestMemmap as test_humidity_Memmap
from PseudoNetCDF.camxfiles.humidity.Read import TestRead as test_humidity_Read
from PseudoNetCDF.camxfiles.ipr.Memmap import TestMemmap as test_ipr_Memmap
from PseudoNetCDF.camxfiles.ipr.Read import TestRead as test_ipr_Read
from PseudoNetCDF.camxfiles.irr.Read import TestRead as test_irr_Read
from PseudoNetCDF.camxfiles.irr.Memmap import TestMemmap as test_irr_Memmap
from PseudoNetCDF.camxfiles.landuse.Memmap import TestMemmap as test_landuse_Memmap
from PseudoNetCDF.camxfiles.lateral_boundary.Memmap import TestMemmap as test_lateral_boundary_Memmap
from PseudoNetCDF.camxfiles.one3d.Memmap import TestMemmap as test_one3d_Memmap
from PseudoNetCDF.camxfiles.one3d.Read import TestRead as test_one3d_Read
from PseudoNetCDF.camxfiles.point_source.Memmap import TestMemmap as test_point_source_Memmap
from PseudoNetCDF.camxfiles.point_source.Read import TestRead as test_point_source_Read
from PseudoNetCDF.camxfiles.temperature.Memmap import TestMemmap as test_temperature_Memmap
from PseudoNetCDF.camxfiles.temperature.Read import TestRead as test_temperature_Read
from PseudoNetCDF.camxfiles.uamiv.Memmap import TestMemmap as test_uamiv_Memmap
from PseudoNetCDF.camxfiles.uamiv.Read import TestuamivRead as test_uamiv_Read
from PseudoNetCDF.camxfiles.uamiv.Write import TestMemmaps as test_uamiv_Write
from PseudoNetCDF.camxfiles.vertical_diffusivity.Memmap import TestMemmap as test_vertical_diffusivity_Memmap
from PseudoNetCDF.camxfiles.vertical_diffusivity.Read import TestRead as test_vertical_diffusivity_Read
from PseudoNetCDF.camxfiles.wind.Memmap import TestMemmap as test_wind_Memmap
from PseudoNetCDF.camxfiles.wind.Read import TestRead as test_wind_Read
