# GX Community Demo 2024-04-16


## Project Structure

* `data/`: csv assets to be used by pandas filesystem assets
* `scripts/`: setup scripts
* `demos/`: full, working versions of demos as jupyter notebooks

## Getting started
* Install requirements

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
