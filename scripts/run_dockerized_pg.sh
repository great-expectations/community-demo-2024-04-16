#!/bin/sh

docker run -d -it --rm -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=demo -e PGDATA=/var/lib/postgresql/data/pgdata --mount type=bind,source=${PWD}/pg16data,target=/var/lib/postgresql/data -h pg postgres:16
