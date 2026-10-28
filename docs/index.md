---
title: obs4MIPs
summary: Home for obs4MIPs
sidebar_title: Home
---

!!! Warning
    These docs are in active development while we are updating the processes for submissions

## 1. Background to obs4MIPs

Obs4MIPs makes observational data more accessible for climate model
evaluation, development and research. It does this by providing observational products
technically aligned with climate model data, such as the World Climate Research Programme's (WCRP)
[Coupled Model Intercomparison Project (CMIP)](https://wcrp-cmip.org/).

Version controlled obs4MIPs compliant datasets provide the foundation for this work.
Some of these products are made available via [ESGF](https://metagrid.esgf-west.org/search), with version control and other registered content managed on
[a separate Github repository](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables).  

Obs4MIPs is a part of the World Climate Research Programme's 
Earth System Modelling and Observations project [ESMO](https://www.wcrp-esmo.org/projects-and-panels).
The obs4MIPs Steering Group is supported by the 
[CMIP](https://wcrp-cmip.org/cmip-governance/project-office/) International Project Office.

#### 1.1 Contact information

Contact the obs4MIPs team at: <b><a href="mailto:submissions-obs4mips@wcrp-cmip.org">submissions-obs4mips@wcrp-cmip.org</a></b>.

#### 1.2 Links to resources

- Obs4MIPs [WRCP-ESMO website](https://www.wcrp-esmo.org/projects-and-panels/obs4mips/obs4mips)
- Obs4MIPs Dataset [proposal form](https://bit.ly/obs4MIPs-submit) 
- Obs4MIPs Data Specifications [ODS](https://doi.org/10.5281/zenodo.11500473)
- Obs4MIPs Datasets searchable on the Earth System Grid Federation [ESGF](https://metagrid.esgf-west.org/search?project=obs4MIPs)
- Obs4MIPs list of datasets organised by product and thematic category on the [UCAR website](https://climatedataguide.ucar.edu/climate-data/obs4mips-observations-model-intercomparisons-project)


## 2. obs4MIPs proposal process

#### 2.1 Summary
##### Making the process of preparing obs4MIPs-compliant products transparent

The required metadata and codes used to prepare obs4MIPs products are developed and maintained in the [CV's](https://github.com/WCRP-ESMO/obs4MIPs_CVs) and [CMOR-tables](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables) public repositories (see the links on the side panel).
Subdirectories (under obs4MIPs-cmor-tables/inputs), corresponding to obs4MIPs _institution_ids_, identify at which institution specific obs4MIPs products are prepared. When multiple products are prepared at the same institution, a deeper level of subdirectories (also denoted with _institution_ids_) indicate the origins of a particular product. These files are useful to copy when preparing an obs4MIPs compliant dataset, as they have been processed and made accessible on ESGF. 

##### Recipe for the preparation of obs4MIPs compliant data

The steps below describe the process of preparing an obs4MIPs-compliant dataset. This often involves copying information from [provided demos](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables/tree/master/demo) and modifying as necessary to prepare a new obs4MIPs-compliant dataset. 
**Please check out our [How-to-Guides](https://wcrp-esmo.github.io/obs4MIPs/how-to-guides/guides/) on the side panel which have links to Scribe instructions**

Although we recommended that obs4MIPs-compliant data products be prepared with the [Climate Model Output Rewriter (**CMOR**)](https://www.wcrp-esmo.org/projects-and-panels/obs4mips/obs4mips_and_cmor_v6-3.pdf), obs4MIPs does support other tools for dataset preparation, e.g. ESMValTool. CMOR is used by most CMIP modelling groups to prepare their model output before publishing it to ESGF. Use of CMOR means compliance with the obs4MIPs data specifications [**ODS**](https://doi.org/10.5281/zenodo.1150047). By preparing a simple "runCmor" [python](https://python.org) script and an input [**JSON**](https://json.org) file, CMOR can be used to prepare an obs4MIPs-compliant dataset.  

CMOR can be obtained [via conda-forge](https://cmor.llnl.gov/mydoc_cmor3_conda/), a community-led collection of infrastructure and distributions for the [conda package manager](https://docs.conda.io/projects/conda/en/latest). 

---

##### Recipe

1) _*Identify an ESGF node to publish your obs4MIPs dataset.*_ Before data are prepared to be made obs4MIPs compliant, the proposer should identify a node within ESGF that can publish the data to make it searchable via Metagrid. If you require help in finding a node, please contact the obs4MIPs team.

2) [Fill out the data proposal form](https://bit.ly/obs4MIPs-submit). Please ask us if you have any questions about the requested information and check out the user guide we have prepared. See the [How-to-Guides](https://wcrp-esmo.github.io/obs4MIPs/how-to-guides/guides/) and the links on the side bar.

3) _*Register a new source_id*_. An issue can be [submitted](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables/issues/new) on this GitHub repo with a proposed _source_id_. The obs4MIPs team will review this information and enter it into the obs4MIPs database of _source_id's_ or propose an alternative if it does not conform to the obs4MIPs data specifications.  When opening an issue, replace the information in the example with your proposed _source_id_. The _source_id_ is intended to identify the product/version and should resemble an existing identifier, but may be modified to be consistent with CMIP/obs4MIPs conventions. For example: A compliant _source_id_ for _GPCP 2.4_ is _GPCP-2-4_. More information on the guidelines for constructing a _source_id_ is available in **Table 1** of the obs4MIPs data specifications [ODS2.6](https://zenodo.org/records/17789550).

4) _*Prepare input table for running CMOR*_. [An example input table](https://github.com/PCMDI/obs4MIPs-cmor-tables/blob/master/demo/demo-global2D/CMAP-V1902.json).  The simplest thing to do is to save this file, rename it, and replace the demo content with the relevant information for a new _source_id_ or dataset. Typically, this involves only making changes to the following attributes:  _contact_, _grid_, _grid_label_, _institution_id_, _nominal_resolution_, _references_, _outpath_, _source_id_, _title_, _variant_info_ and _variant_label_. All obs4MIPs products should clearly identify the origins of the data (where and when did the person preparing the obs4MIPs compliant product obtain the original data). This information can be documented in the last three attributes of the example input table identified above via the following attributes: _originData_URL_, _originData_retrieved_, and _originData_notes_.

5) _*Prepare python script for reading in data an writing with CMOR*_. This is the most time consuming aspect of preparing an obs4MIPs-compliant data set. It involves preparing a simple Python script to read the original data downloaded in advance. As with the steps before, start by downloading a [demo python script](https://github.com/PCMDI/obs4MIPs-cmor-tables/blob/master/demo/runCMORdemo_CMAP-V1902.py), renaming it accordingly, and modifying. The examples provided illustrate how data already in netCDF can be processed to be obs4MIPs compliant, but in principle, input data in other formats can be used if the user can process the data using CMOR. [**An example**](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables/tree/master/demo/demo-global2D) input table and script using xarray and CMOR.

6) _*Execute script.*_ The processed data is located in a directory defined in the input_table: outpath + output_path_template, the former being the base directory (where the user wants to output the data) and the latter a directory template explicitly defined for obs4MIPs _<activity_id>/<institution_id>/<source_id>/<frequency>/<variable_id>/<grid_label>/<version>_ which should not be altered.
   
7) Perform quality control on the obs4MIPs-compliant dataset. The obs4MIPs [QA/QC](https://github.com/WCRP-ESMO/cc-plugin-obs4mips) tool is under development, and should be considered a beta release. This tool will be a mandatory step for publication to ESGF. 
  
8) _*Create an issue to include the processing code in this repository.*_  **Please note a dataset is not obs4MIPs-compliant unless the source_id is registered and the input json and python scripts used for processing are included in this repo.**  This ensures transparency in the obs4MIPs process. 

**Note the above process of preparing obs4MIPs-compliant data is in support of, but independent of the process of publishing obs4MIPs-compliant data to ESGF.**  

#### 2.2 Simple flow chart of the obs4MIPs process

<!-- use mermaid? https://squidfunk.github.io/mkdocs-material/reference/diagrams/ -->

<!-- ### To add:
- how-to guides - proposal and airtable links
- examples - [inputs folder](https://github.com/WCRP-ESMO/obs4MIPs-cmor-tables/tree/master/inputs) 
- other repos: will be moving to using [obs4MIPs CVs](https://github.com/WCRP-ESMO/obs4MIPs_CVs)
- proposal timeline info - workflow overview. 
- capturing issues with data preperation, using CMOR
- esgf publication steps
- diagram/ flow on QA/QC process -->
