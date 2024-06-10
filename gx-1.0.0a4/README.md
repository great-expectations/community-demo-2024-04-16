# great_expectations 1.0.0a4 demos

Demos of expectation authoring and validation workflows for great-expectations 1.0.

These demos use python 3.10 with [1.0.0a4](https://pypi.org/project/great-expectations/1.0.0a4/).

## Notes about these scripts
The scripts in this directory will run against 1.0.0a4, and include TODOs on future changes planning for subsequent prereleases of 1.0.0.

## Getting started
1. Create a virtual environment: `python -m venv .venv`
1. Source the virtual environment: `source .venv/bin/activate`
1. Install requirements: `pip install -r requirements.txt`
1. Start the postgres container: `../scripts/run_dockerized_pg.sh`
1. Run the notebooks in `demos/`
