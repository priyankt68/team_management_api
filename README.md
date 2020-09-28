# Team Management API

APIs to create, list, update and delete users.

# Setup

## Clone the project
```
git clone https://github.com/priyankt68/team_management_api.git
cd team_management_api
```

## Docker based setup

Ensure that you have a docker daemon running on your system.

### Build

```
docker-compose up --build -d 
```

### Setup the dev environment

The environment variables is present `sample.env.dev`.  Create a new dev envrionment file `.env.dev`.
```
cp sample.env.dev env.dev
```

We can update following variables for PostgreSQL password, user and port.
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=teams_api_db
SQL_USER=teams_api_user
SQL_PASSWORD=some_password
SQL_HOST=db
SQL_PORT=some_non_standard_port_like_5432
```



### Run the containers
```
docker-compose up teams_api
```
You can run `docker ps` to find two containers running. One for teams_api and other for database - Postgresql.

## Database mimgrations

*Create initial migrations*

```
docker exec -it team_management_api_teams_api_1 sh
/usr/src/app # python manage.py migrate 
```

*Create models migrations*
```
docker exec -it team_management_api_teams_api_1 sh
/usr/src/app # python manage.py makemigrations teams
/usr/src/app # python manage.py migrate
```

### Creating superusers for Django Admin
```
docker exec -it team_management_api_teams_api_1 sh
/usr/src/app # python manage.py createsuperuser
```


## Testing APIs

### List all users
```
curl --location --request GET 'http://0.0.0.0:9000/users'
```
### Create new user
```
curl --location --request POST 'http://0.0.0.0:9000/users/' \
--form 'firstName=Bob' \
--form 'lastName=Dylan' \
--form 'phone=783825224' \
--form 'role=regular'
```

### Update a user
```
curl --location --request PUT 'http://0.0.0.0:9000/users/2' \
--form 'firstName=Bobby' \
--form 'lastName=Dylan' \
--form 'phone =7838252412' \
--form 'role=admin'
```

### Delete a user
```
curl --location --request DELETE 'http://0.0.0.0:9000/users/2'
```