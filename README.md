# Flask RestX Boilerplate

An awesome REST boilerplate that uses Flask-RESTX (formerly Flask-RESTPlus).
It has the usual API features to get you started and off the ground,
it's also designed to be easily scalable and extendable.

I wrote this boilerplate because I found that a lot of Flask REST boilerplates are either
doing too much, is lacking, or it simply doesn't fit my needs.

# Features

* JSON Web Token Authentication with [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* Swagger Documentation (Part of Flask-RESTX).
* Unit Testing.
* Database ORM with [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* Database Migrations using [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* Object serialization/deserialization with [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)

# Pre-requisites

This boilerplate uses `SQLite` as its database, make sure you have it installed.
`Pipenv` is recommended to help manage the dependencies and virtualenv.

It uses [Black](https://github.com/psf/black) for code styling/formatting.

# Usage

## Installing
```sh
# Clone the repo
$ git clone https://github.com/X1Zeth2X/flask-restx-boilerplate.git

# Install packages with pipenv
$ pipenv install
```

## Running
Please note that you will need to specify `FLASK_APP` so that Flask CLI knows what to run.

Usually you create `.env` and source from there.

```sh
# .env file
export FLASK_APP=giya

# configs: prod, test, dev
export FLASK_CONFIG=dev
...
```

```sh
# Source your .env file
$ source /path/to/.env

# Enter the virtualenv
$ pipenv shell

# Run the app
$ flask run
```