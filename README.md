Prisoner Money – Start page
===========================

This repository contains the user research content for the ‘Send money to a prisoner’ service.

The live content can be found at [gov.uk/send-prisoner-money](https://www.gov.uk/send-prisoner-money)

In production, this app is used to redirect legacy domains/paths.

Requirements
------------

- Python 3.10

Unlike most Prisoner Money apps, this one does not use the REST api and is built with Flask instead of Django.

Development
-----------

[![CircleCI](https://circleci.com/gh/ministryofjustice/money-to-prisoners-start-page.svg?style=svg)](https://circleci.com/gh/ministryofjustice/money-to-prisoners-start-page)

### Run locally

It's recommended that you use a python virtual environment to isolate each application.

The simplest way to do this is using:

```shell
python -m venv venv              # creates a virtual environment for dependencies; only needed the first time
. venv/bin/activate              # activates the virtual environment; needed every time you use this app
pip install -r requirements.txt  # installs python dependencies; needed whenever requirements are changed
```

```shell
FLASK_DEBUG=1 FLASK_APP=app/app.py flask run
```

### Run locally in Docker

```shell
docker build --tag start-page .
docker run --rm -p 8080:8080 start-page
```

### Run basic tests

```shell
flake8
pytest --capture no
```

Deployment
----------

See [money-to-prisoners-deploy](https://github.com/ministryofjustice/money-to-prisoners-deploy) for instructions
on building and deployment.
