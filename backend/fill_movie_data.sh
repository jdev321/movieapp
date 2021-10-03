#!/bin/sh

d="http://files.tmdb.org/p/exports/movie_ids_10_03_2021.json.gz"

pipe=/tmp/moviefifo

echo "mkfifo $pipe"

request="$(curl "$d" | zcat | jq -r '[.[]] | @csv' >$pipe)"

echo "${request}"

psql -h movie-db -d movie_data_dev -p 5432 -U postgres -c "\copy movie(adult, id, original_title, popularity, video) FROM '$pipe' delimiter ',' CSV"

echo "rm $pipe"