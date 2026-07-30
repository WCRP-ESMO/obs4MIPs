#!/usr/bin/env python
"""
Check the temperature data array dimensions
"""
import xarray as xr
import xcdat as xc
import numpy as np

inputFilePath = '/Users/paul.smith/obs4MIPs-cmor-tables/inputs/NOAA-NCEI/GLODAP-2-2016b/GLODAPv2.2016c.temperature.nc'
inputVarName = 'temperature'

print("="*70)
print("DATA ARRAY DIMENSION CHECK")
print("="*70)

# Open file
f = xc.open_dataset(inputFilePath, decode_times=False)
d = f[inputVarName]

print(f"\nVariable: {inputVarName}")
print(f"Shape: {d.shape}")
print(f"Dimensions: {d.dims}")
print(f"Data type: {d.dtype}")

print(f"\nCoordinate information:")
for dim in d.dims:
    coord = f[dim]
    print(f"  {dim}: size={coord.size}, values range=[{coord.values.min():.2f}, {coord.values.max():.2f}]")

print(f"\nExpected dimension order for CMOR with axes=[olevel, lat, lon]:")
print(f"  Should be: (depth, lat, lon) = (33, 180, 360)")
print(f"  Actually is: {d.dims} = {d.shape}")

if d.dims == ('depth', 'lat', 'lon'):
    print("✓ Dimension order matches!")
elif d.dims == ('lat', 'lon', 'depth'):
    print("✗ ERROR: Dimension order is wrong! Need to transpose.")
    print("  Use: d = d.transpose('depth', 'lat', 'lon')")
else:
    print(f"✗ ERROR: Unexpected dimension order: {d.dims}")

print("\n" + "="*70)
