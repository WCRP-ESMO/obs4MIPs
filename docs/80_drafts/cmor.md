---
title: CMOR
summary: Demos with CMOR
sidebar_title: CMOR
---

From [demo in old repo](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables/tree/master/demo)

The software and utilites used in this demo are available via [Anaconda](https://continuum.io) and include:

- **CMOR**
    - https://cmor.llnl.gov
    - https://anaconda.org/conda-forge/cmor

- **xarray**
    - https://docs.xarray.dev/en/stable
    - https://anaconda.org/conda-forge/xarray 

- **xcdat**
    - https://xcdat.readthedocs.io/en/stable
    - https://anaconda.org/conda-forge/xcdat

An environment called `MYENVNAME` including the above software can be installed from conda-forge with the following single command:

```
conda create -n MYENVNAME -c conda-forge xarray cmor xcdat
```

Running the demos, python code reads in the sample data via xarray, generates grid bounds via xcdat, and outputs a demo file using CMOR.  The demos must be run with CMOR 3.2.6 or a more recent version.  To run each demo, all contents in the demo subdirectory (including the /Tables subdirectory) must be saved locally, and a conda envirnment must be created including CMOR, xarray and xcdat. If python needs to be installed, it too is available via [anaconda](https://anaconda.org/conda-forge/python). Once that is done, execute the following:

- **demo-global2D**
    
`python runCMORdemo_CMAP-V1902.py`

- **demo-insitu**

`python insitu_CMOR_demo.py`

- **demo-zonalmeans**

`python runCMORdemo_zonalmean.py`

<!-- If you have any difficulties, please contact the obs4MIPs team at obs4MIPs-admin@llnl.gov

[More details on the process of preparing obs4MIPs compliant data are available in /inputs of this repo.](https://github.com/PCMDI/obs4MIPs-cmor-tables/tree/master/inputs/README.md) -->
