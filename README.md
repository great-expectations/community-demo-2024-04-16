# 1.0.0 Prerelease Demos

## About this repository

The included scripts and notebooks are intended to give a quick look at API changes in 1.0.0.
Scripts that use postgres all use the same postgres image described below.
Demos and scripts are found under the associated `gx-<VERSION>` directory, and a corresponding `requirements.txt` is included in each that pins the great_expectations version.

### Additional steps for Macs with Apple Silicon (e.g. M1)
You may need to run these additional steps
* pip uninstall psycopg2
* brew install libpq --build-from-source
* export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"
* pip install psycopg2-binary

## Project Structure

* `gx-*/`
  * `demos/notebooks`: full, working versions of demos as notebooks
  * `demos/scripts`: full, working python scripts
  * `requirements.txt`: requirements files for the specific version
* `scripts/`: setup scripts

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
