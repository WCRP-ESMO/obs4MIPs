## Contributing to docs for obs4MIPS

- These are generated using [mkdocs](https://www.mkdocs.org/) with theme [mkdocs-shadcn](https://asiffer.github.io/mkdocs-shadcn/)

- `docs` folder with subpages folders, assets and stylesheets.
- `mkdocs` folder has mkdocs.yml with navigation structure and requirements.txt for deployment

### Development
- clone this repo and have a python environment you can use, e.g. use a virtual environment (on linux):
```
python -m venv .venv
source .venv/bin/activate
pip install -r mkdocs/requirements.txt
```

- build locally with your python environment by cloning this repo and running: 
```
mkdocs serve -f mkdocs/mkdocs.yml
```
- will likely be served at an address such as `http://127.0.0.1:8000/` which you can open in your browser

### References
Initially copied the mkdocs.yml and stylesheets from https://github.com/WCRP-CMIP/cmip7-guidance/tree/docs 
to align look and feel.