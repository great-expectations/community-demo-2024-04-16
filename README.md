# GX Community Demo 2024-04-16

Demos of expectation authoring and validation workflows for great-expectations 1.0.

These demos use python 3.10 with [1.0.0a2](https://pypi.org/project/great-expectations/1.0.0a2/).

## Getting started
1. Create a virtual environment: `python -m venv .venv`
1. Source the virtual environment: `source .venv/bin/activate`
1. Install requirements: `pip install -r requirements.txt`
1. Start the postgres container: `./scripts/run_dockerized_pg.sh`
1. Run the notebooks in `demos/`

## Project Structure

* `scripts/`: setup scripts
* `demos/`: full, working versions of demos as jupyter notebooks


## Running PostgreSQL

We've prepared a dockerized PostgreSQL with sample data that you can run with the command:
```
./scripts/run_dockerized_pg.sh
```

If you want to connect to the database to manually execute SQL queries you can run:
```
./scripts/psql_dockerized_postgres.sh
```
This `psql` script has the connection string if you would like to use a different tool to connect to the database.
