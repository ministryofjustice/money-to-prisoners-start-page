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

See [money-to-prisoners-deploy](https://github.com/ministryofjustice/money-to-prisoners-deploy) for instructions on deployment.

Build image for Cloud Platform and push to ECR:

```bash
export ECR_URL=????  # get from kubernetes secret "ecr" > "repo_url"

export APP=start-page
export APP_GIT_COMMIT=$(git rev-parse HEAD)
export APP_GIT_COMMIT_SHORT=${APP_GIT_COMMIT:0:7}
export APP_BUILD_TAG=${APP}.${APP_GIT_COMMIT_SHORT}
export APP_BUILD_DATE=$(date +%FT%T%z)

docker build \
  --build-arg APP_GIT_COMMIT=${APP_GIT_COMMIT} \
  --build-arg APP_BUILD_TAG=${APP_BUILD_TAG} \
  --build-arg APP_BUILD_DATE=${APP_BUILD_DATE} \
  --tag ${APP} .
docker tag ${APP} ${ECR_URL}:${APP}
docker tag ${APP} ${ECR_URL}:${APP_BUILD_TAG}
docker push ${ECR_URL}:${APP}
docker push ${ECR_URL}:${APP_BUILD_TAG}
```
