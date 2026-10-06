# Data UI

A Django-powered interface for newsroom data at the Star Tribune. Used for internal purposes.

## Data management

Data management happens through the Django Admin, which is at `/admin/`.

## API

An API has been exposed for each model. Each request requires a `username` and `api-key`.

- `/api/v01/company_details/`: Custom endpoint for Companies and their connected records. Note that these are slow endpoints.
  - `/api/v01/company_details/?coid=1234&limit=100&username=XXXXXX&api_key=XXXXXX`
  - Use the custom filter `finance_publishyear` to get companies that have a Finance record for that year. For example:
    - `/api/v01/company_details/?finance_publishyear=2018&limit=100&username=XXXXXX&api_key=XXXXXX`
  - Use the custom filter `nonprofit_finance_publishyear` to get companies that have a Finance record for that year. For example:
    - `/api/v01/company_details/?nonprofit_finance_publishyear=2017&limit=10&username=XXXXXX&api_key=XXXXXX`

## Development

### Prerequisites

- Python 3.12 (pinned in `.python-version`)
- [uv](https://docs.astral.sh/uv/)
  - `brew install uv`

### Settings

Settings that are unique to the environment are managed with environment variables. You can manage these how you want, or you can use a `.env` file. The following variables are required or suggested to be set.

1.  `DEBUG`: `True` or `False`, defaults to false.
    - Have run into issues where the [Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) slows down the page significantly, so this is a separate `DEBUG_TOOLBAR` variable.
1.  `SECRET_KEY`: Random, unique string
1.  `DEFAULT_DB_URI`: Database URI for the default database that manages users, something like `database-type://user:pass@host:port/database-name`, defaults to a local SQLite file.
1.  `DATADROP_BUSINESS_DB_URI`: Database URI for the business companies database, something like `mysql://user:pass@host:3306/database-name`
1.  `TIME_ZONE`: Defaults to `America/Chicago`
1.  `STATIC_ROOT`: Defaults to local `static-assets/` directory.

#### MySQL connections and TLS

The MySQL databases run on AWS RDS (MySQL 8.4), which requires encrypted connections. MySQL connections use TLS and verify the server's certificate against the AWS RDS CA bundle in `data_ui/certs/rds-global-bundle.pem` (see `data_ui/settings.py`).

Because the certificate is checked against the hostname, MySQL URIs must use the RDS endpoint, not a custom DNS alias. For example, use `news-data-cluster.cluster-cgbgcwbxiden.us-east-2.rds.amazonaws.com`, not `news-data.stribapps.com`. Using the alias fails with `certificate verify failed: Hostname mismatch`.

The app talks to MySQL through [PyMySQL](https://github.com/PyMySQL/PyMySQL), a pure-Python driver installed as `MySQLdb`, so no native MySQL client libraries are needed.

### Environment

1.  `uv sync`
1.  `uv run python manage.py migrate && uv run python manage.py migrate --database=datadrop_business`
1.  For first time setup, create an admin user: `uv run python manage.py createsuperuser`
1.  `uv run python manage.py collectstatic`

### Running locally

1.  `uv run python manage.py runserver`

- This will start a webserver at [localhost:8000](http://127.0.0.1:8000/).

### New dataset

For each dataset, we make a new Django "app". For instance, say we have a campaign finance database that we want to hook up.

1.  `uv run python manage.py startapp campaign_finance`
    - Creates a new directory for the app with some basics
1.  Create models based on the database and all the tables in it
    - `uv run python manage.py inspectdb --database="campaign_finance_db" > campaign_finance/models.py`
    - You can add options to `inspectdb` to only get specific tables.
1.  ...

## Deployment

The app is deployed "serverless" style to AWS Lambda using the
[Zappa library](https://github.com/zappa/Zappa).

### Settings

See settings above. Env variables need to be set in the configuration
tab of the Lambda function. Additionally, settings specific to the Lambda
functions can be found in `zappa_settings.json`.

### Deploy

To deploy the current version of the app to Zappa, run

```
uv run zappa update <stage name>
```

We currently have `dev` and `prod` stages, both deployed to `us-east-2` with the `newsroom-aws` AWS profile.

To create a new stage, add it to `zappa_settings.json` and run

```
uv run zappa deploy <stage name>
```
