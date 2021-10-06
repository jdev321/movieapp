### Project setup
```
docker-compose up -d --build

docker-compose exec web python app/db.py

docker-compose exec web aerich upgrade

docker-compose exec web fill_movie_data.sh(Will ask you for password)

127.0.0.1:8004/docs to see the endpoints
```

### Database
```
To see the database

docker-compose exec movie-db psql -U postgres

\c movie_data_dev

\dt to see the tables

docker-compose exec movie-db psql -U postgres -d movie_data_dev -c "SELECT * FROM movie LIMIT 5

Run above command after building the database to ensure data is in there

```