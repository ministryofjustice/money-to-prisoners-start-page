import json
import os

APP = 'start-page'
ENVIRONMENT = os.environ.get('ENV') or 'local'

APP_GIT_COMMIT = os.environ.get('APP_GIT_COMMIT') or 'unknown'
APP_GIT_COMMIT_SHORT = APP_GIT_COMMIT[:7]
APP_BUILD_TAG = os.environ.get('APP_BUILD_TAG') or 'unknown'
APP_BUILD_DATE = os.environ.get('APP_BUILD_DATE') or 'unknown'

SEND_MONEY_URL = os.environ.get('PUBLIC_SEND_MONEY_HOST')
if SEND_MONEY_URL:
    SEND_MONEY_URL = f'https://{SEND_MONEY_URL}'
else:
    SEND_MONEY_URL = 'http://localhost:8004'

TEMPLATE_CONTEXT = dict(
    APP=APP,
    ENVIRONMENT=ENVIRONMENT,

    APP_GIT_COMMIT=APP_GIT_COMMIT,
    APP_GIT_COMMIT_SHORT=APP_GIT_COMMIT_SHORT,
    APP_BUILD_TAG=APP_BUILD_TAG,
    APP_BUILD_DATE=APP_BUILD_DATE,

    SEND_MONEY_URL=SEND_MONEY_URL,
)
PING_JSON = json.dumps(dict(
    build_date=APP_BUILD_DATE,
    commit_id=APP_GIT_COMMIT,
    version_number=APP_BUILD_TAG,
))

METRICS_USER = os.environ.get('METRICS_USER', 'prom')
METRICS_PASS = os.environ.get('METRICS_PASS', 'prom')

if os.environ.get('SENTRY_DSN'):
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(
        dsn=os.environ['SENTRY_DSN'],
        integrations=[FlaskIntegration()],
        environment=ENVIRONMENT,
        release=APP_GIT_COMMIT or 'unknown',
        send_default_pii=False,
        traces_sample_rate=1.0,
    )
