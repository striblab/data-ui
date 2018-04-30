# Data UI

A Django-powered interface for newsroom data at the Star Tribune.  Used for internal purposes.

## Development

### Prerequisites

* Python 3.6+
* [pipenv](https://docs.pipenv.org/)
    * `brew install pipenv`
    * Or `pip install pipenv --user`

### Settings

1. Copy the example settings file: `cp settings_local.example.py settings_local.py`
1. Edit `settings_local.py` with the appropriate values.

### Environment

1.  `pipenv shell`
1.  `pipenv install`
1.  `python manage.py migrate && python manage.py migrate --database=datadrop_business`

### Running locally

1.  `python manage.py runserver`
  * This will start a webserver at [localhost:8000](http://127.0.0.1:8000/).

### New dataset

For each dataset, we make a new Django "app".  For instance, say we have a campaign finance database that we want to hook up.

1.  `python manage.py startapp campaign_finance`
    * Creates a new directory for the app with some basics
1.  Create models based on the database and all the tables in it
    * `python manage.py inspectdb --database="campaign_finance_db" > campaign_finance/models.py`
    * You can add options to `inspectdb` to only get specific tables.
1. ...
