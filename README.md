# Data UI

A Django-powered interface for newsroom data at the Star Tribune. Used for internal purposes.

## Development

### Prerequisites

* Python 3.6+
* [pipenv](https://docs.pipenv.org/)
  * `brew install pipenv`
  * Or `pip install pipenv --user`

### Settings

Settings that are unique to the environment are managed with environment variables. You can manage these how you want, or you can use a `.env` file. The following variables are required or suggested to be set.

1.  `DEBUG`: `True` or `False`, defaults to false.
1.  `SECRET_KEY`: Random, unique string
1.  `DEFAULT_DB_URI`: Databsase URI for the default database that manages users, something like `database-type://user:pass@host:port/database-name`, defaults to a local SQLite file.
1.  `DATADROP_BUSINESS_DB_URI`: Databsase URI for the business companies database, something like `mysql://user:pass@host:3306/database-name`
1.  `TIME_ZONE`: Defaults to `America/Chicago`
1.  `STATIC_ROOT`: Defaults to local `static-assets/` directory.

### Environment

1.  `pipenv shell`
1.  `pipenv install`
1.  `python manage.py migrate && python manage.py migrate --database=datadrop_business`
1.  `python manage.py collectstatic`

### Running locally

1.  `python manage.py runserver`

* This will start a webserver at [localhost:8000](http://127.0.0.1:8000/).

### New dataset

For each dataset, we make a new Django "app". For instance, say we have a campaign finance database that we want to hook up.

1.  `python manage.py startapp campaign_finance`
    * Creates a new directory for the app with some basics
1.  Create models based on the database and all the tables in it
    * `python manage.py inspectdb --database="campaign_finance_db" > campaign_finance/models.py`
    * You can add options to `inspectdb` to only get specific tables.
1.  ...

## Deploy

Deployment is managed with Docker.
