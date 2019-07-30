# flight-booking-application

[![Build Status](https://travis-ci.org/PatrickCmd/flight-booking-application.svg?branch=develop)](https://travis-ci.org/PatrickCmd/flight-booking-application)
[![Coverage Status](https://coveralls.io/repos/github/PatrickCmd/flight-booking-application/badge.svg?branch=develop)](https://coveralls.io/github/PatrickCmd/flight-booking-application?branch=develop)

## TECHNOLOGIES USED
- **Python3.6**: [Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively
- **Django 2.2**: [Django](https://docs.djangoproject.com/en/2.2/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework**: [Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs
- **Django REST framework JWT**: [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework.
- **Django REST Swagger**: [Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger) An API documentation generator for Swagger UI and Django REST Framework.
- **Postgresql**: [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- **Pipenv**: [Pipenv](https://docs.pipenv.org/) is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.
- **Psycopg2**: [Psycopg](http://initd.org/psycopg/) is the most popular PostgreSQL adapter for the Python programming language.

## API Documentation
Visit the links below for the API documentation

[CoreApi Documentation](https://flight-booking-system-api.herokuapp.com/docs)

## Live API
Vist this [Link](https://flight-booking-system-api.herokuapp.com/) for the live application.

## SETTING UP THE PROJECT

### Clone the project
```
$ https://github.com/PatrickCmd/flight-booking-application.git
$ cd flight-booking-application
```

### Active the virtual environment
```
$ pip install pipenv
$ pipenv shell
```

### Install the requirements
```
$ pipenv install
```

## SETTING UP THE DATABASE
Execute the commands in the terminal/console as stated below

### ON WINDOWS
Follow the [Link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) on how to download 
and install postgres(>=10) on windows platform

**Create Database**
```
$ psql -U postgres
$postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ Rename env.example to .env and change the content as per your development settings
```

### ON MAC/UBUNTU
**Install postgres**

**MAC Users**
```
$ brew install postgres
```
Follow the [link](https://brew.sh/) on how to setup brew if not yet installed

**Ubuntu users**

Follow the [Link](https://www.postgresql.org/download/linux/ubuntu/) on how to setup 
and install postgres(>=10) on Ubuntu-linux platform

**Create Database**
```
$ psql -U postgres
$ postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ Rename env.example to .env and change the content as per your development settings
```

## Run database migrations and create superuser
```
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run the server
```
$ python manage.py runserver_plus
```
Execute the url **localhost:8000/** in your browser

## Run tests
Execute this command at the terminal
```
$ python manage.py test
```

## TESTING THE API
### API URL ENDPOINTS
#### Register users: Methods['POST'] `http://localhost:8000/fbs-api/users/`
```
{   "email": "example.example@andela.com",
    "password": "Example1234#",
    "date_of_birth": "1900-11-19",
    "first_name": "Example",
    "middle_name": "",
    "last_name": "Example Last",
    "gender": "m",
    "location": "Kyebando",
    "phone": "256786893374"
}
```
#### Login user: Methods['POST'] `http://localhost:8000/fbs-api/users/login/`
```
{	
    "email": "example.example@andela.com",
    "password": "Example234#"
}
```
#### Create user profile: Methods['POST'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/profiles/`
```
{	
    "using_country": "KENYA",
    "country_of_citizenship": "KENYA",
    "passport_number": "K510192823",
    "issue_date": "2018-08-08",
    "expiration_date": "2028-08-08",
    "passport_photo": ""
}
```
#### Profile Details: Methods['GET', 'PUT/PATCH', 'DELETE'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/profiles/4/`

#### Upload passport photo: Methods['POST'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/profiles/4/`
```
Form data
{
    'passport_photo': 'file.png or file.jpg'
}
```
#### Create Flight Admins[Superusers] only: Methods['POST'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/`
```
{
    "name": "Entebbe to Denver",
    "origin": "Entebbe",
    "destination": "Denver",
    "departure": "2019-08-02T08:00:00Z",
    "arrival": "2019-08-03T07:00:00Z",
    "aircraft": "Vintage",
    "status": "ON_TIME",
    "number": "KPQYWT72839",
    "capacity": 120
}
```

##### Flight Details Admins[Superusers] only: Methods['PUT', 'DELETE'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/<id>`
```
{
    "name": "Entebbe to Denver",
    "origin": "Entebbe",
    "destination": "Denver",
    "departure": "2019-08-02T08:00:00Z",
    "arrival": "2019-08-03T07:00:00Z",
    "aircraft": "Vintage",
    "status": "ON_TIME",
    "number": "KPQYWT72839",
    "capacity": 120
}
```

#### Get flight: Methods['GET'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/<id>`

#### Make Reservation: Methods['POST'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/<id>/reservation`

```
{
    'seat': 'A6'
}
```

#### See Reservation: Methods['GET'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/<id>/reservation/<id>`

#### Cancel Reservation: Methods['PATCH'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/flights/<id>/reservation/<id>/cancel`

#### Number of Reservation on given day for a given flight: Methods['GET'] Authorization JWT-TOKEN token `http://localhost:8000/fbs-api/reservations/<flight_pk>/count/<date>/`