#!/usr/bin/env python
"""
Investigate the depth coordinate in detail
"""
import xarray as xr
import xcdat as xc
import numpy as np

inputFilePath = '/Users/paul.smith/obs4MIPs-cmor-tables/inputs/NOAA-NCEI/GLODAP-2-2016b/GLODAPv2.2016c.temperature.nc'

print("="*70)
print("DETAILED DEPTH COORDINATE INVESTIGATION")
print("="*70)

# Open file
f = xc.open_dataset(inputFilePath, decode_times=False)

print("\nAll variables in the file:")
for var in f.variables:
    print(f"  {var}: {f[var].shape}")

print("\nAll coordinates:")
for coord in f.coords:
    print(f"  {coord}: {f.coords[coord].shape}")

print("\n" + "="*70)
print("DEPTH COORDINATE DETAILS")
print("="*70)

if 'depth' in f.coords:
    depth_coord = f.coords['depth']
    print(f"\nDepth as coordinate:")
    print(f"  Shape: {depth_coord.shape}")
    print(f"  Values: {depth_coord.values}")
    print(f"  Dtype: {depth_coord.dtype}")
    print(f"  Attributes: {depth_coord.attrs}")

if 'depth' in f.variables:
    depth_var = f['depth']
    print(f"\nDepth as variable:")
    print(f"  Shape: {depth_var.shape}")
    print(f"  Values: {depth_var.values}")
    print(f"  Dtype: {depth_var.dtype}")
    print(f"  Attributes: {depth_var.attrs}")

print("\n" + "="*70)
print("HOW TO ACCESS DEPTH VALUES")
print("="*70)

# Try different ways to access depth
print("\n1. f.depth.values:")
print(f"   {f.depth.values}")

print("\n2. f['depth'].values:")
print(f"   {f['depth'].values}")

print("\n3. f.coords['depth'].values:")
print(f"   {f.coords['depth'].values}")

# Check if there's a depth_surface or other depth variable
print("\n" + "="*70)
print("CHECKING FOR OTHER DEPTH-RELATED VARIABLES")
print("="*70)
depth_related = [v for v in f.variables if 'depth' in v.lower() or 'lev' in v.lower()]
for var in depth_related:
    print(f"\n{var}:")
    print(f"  Shape: {f[var].shape}")
    print(f"  Values: {f[var].values}")

print("\n" + "="*70)
