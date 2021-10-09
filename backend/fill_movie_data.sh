#!/bin/sh

# Script to fill postgresql database with movie data from themoviedb daily export files.
# Will check if file for today's date exists. If not, will check for day before.

today="$(date +'%m_%d_%Y')"

if curl --output /dev/null --silent --head --fail "$url"; then
    echo "Grabbing daily export file for date: $today"
else
    echo "Daily export file for $today does not exist."
    today="$(date --date=' 1 days ago' '+%m_%d_%Y')"
    echo "Grabbing daily export file for date: $today"
fi

url="http://files.tmdb.org/p/exports/movie_ids_${today}.json.gz"

pipe=/tmp/moviefifo

echo "mkfifo $pipe"

request="$(curl "$url" | zcat | jq -r '[.[]] | @csv' >$pipe)"

echo "${request}"

psql -h movie-db -d movie_data_dev -p 5432 -U postgres -c "\copy movie(adult, id, original_title, popularity, video) FROM '$pipe' delimiter ',' CSV"

echo "rm $pipe"