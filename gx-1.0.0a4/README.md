# great_expectations 1.0.0a4 demos

Demos of expectation authoring and validation workflows for great-expectations 1.0.

These demos use python 3.10 with [1.0.0a4](https://pypi.org/project/great-expectations/1.0.0a4/).

## Notes about these demos

* The scripts in this directory will run against 1.0.0a4, and include TODOs on future changes planning for subsequent prereleases of 1.0.0.
* To run the `demos/scripts/*.py` scripts, one must have valid AWS credentials for free access to the [New York City Taxi Data Set](https://registry.opendata.aws/nyc-tlc-trip-records-pds/) since it is served from S3. See the linked data set description for more information.

## Getting started
1. Create a virtual environment: `python -m venv .venv`
2. Source the virtual environment: `source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Start the postgres container: `../scripts/run_dockerized_pg.sh`
5. Run the notebooks and scripts in `demos/`
