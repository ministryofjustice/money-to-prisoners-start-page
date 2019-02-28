Prisoner Money – Start page
===========================

This repository contains the user research content for the ‘Send money to a prisoner’ service.

The live content can be found at [gov.uk/send-prisoner-money](https://www.gov.uk/send-prisoner-money)

Development
-----------

Run locally:

```bash
FLASK_APP=app/app.py flask run
```

Run locally in Docker:

```bash
docker build --tag start-page .
docker run --rm -p 80:80 start-page
```

Deployment
----------

See [money-to-prisoners-deploy](https://github.com/ministryofjustice/money-to-prisoners-deploy) for instructions
on building and deployment.
