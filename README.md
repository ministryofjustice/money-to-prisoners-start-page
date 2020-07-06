Prisoner Money – Start page
===========================

This repository contains the user research content for the ‘Send money to a prisoner’ service.

The live content can be found at [gov.uk/send-prisoner-money](https://www.gov.uk/send-prisoner-money)

In production, this app is used to redirect legacy domains/paths.

Requirements
------------

- Python 3.6+

Unlike most Prisoner Money apps, this one does not use the REST api.

Development
-----------

Run locally:

```shell script
FLASK_ENV=development FLASK_APP=app/app.py flask run
```

Run locally in Docker:

```shell script
docker build --tag start-page .
docker run --rm -p 8080:8080 start-page
```

Deployment
----------

See [money-to-prisoners-deploy](https://github.com/ministryofjustice/money-to-prisoners-deploy) for instructions
on building and deployment.
