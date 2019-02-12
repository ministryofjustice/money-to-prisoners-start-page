import json
import os

from flask import Flask, Response, redirect, render_template

APP = 'start-page'
ENVIRONMENT = os.environ.get('ENV', 'local')

APP_GIT_COMMIT = os.environ.get('APP_GIT_COMMIT')
APP_GIT_COMMIT_SHORT = (APP_GIT_COMMIT or 'unknown')[:7]
APP_BUILD_TAG = os.environ.get('APP_BUILD_TAG')
APP_BUILD_DATE = os.environ.get('APP_BUILD_DATE')

SEND_MONEY_URL = os.environ.get('PUBLIC_SEND_MONEY_HOST')
if SEND_MONEY_URL:
    SEND_MONEY_URL = f'https://{SEND_MONEY_URL}'
else:
    SEND_MONEY_URL = 'http://localhost:8004'

app = Flask(__name__)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
)

context = dict(
    APP=APP,
    ENVIRONMENT=ENVIRONMENT,

    APP_GIT_COMMIT=APP_GIT_COMMIT,
    APP_GIT_COMMIT_SHORT=APP_GIT_COMMIT_SHORT,
    APP_BUILD_TAG=APP_BUILD_TAG,
    APP_BUILD_DATE=APP_BUILD_DATE,

    SEND_MONEY_URL=SEND_MONEY_URL,
)


@app.route('/')
def index():
    if ENVIRONMENT == 'prod':
        return redirect('https://www.gov.uk/send-prisoner-money')
    return render_template('index.html', **context)


@app.route('/info')
def info():
    if ENVIRONMENT == 'prod':
        return redirect('https://www.gov.uk/staying-in-touch-with-someone-in-prison')
    return render_template('info.html', **context)


@app.route('/robots.txt')
def robots():
    return Response(
        'User-agent: *\n'
        'Disallow: /',
        content_type='text/plain',
    )


@app.route('/ping.json')
def ping():
    return no_cache(Response(
        json.dumps(dict(
            build_date_key=APP_BUILD_DATE,
            commit_id_key=APP_GIT_COMMIT,
            version_number_key=APP_BUILD_TAG,
        )),
        content_type='application/json',
    ))


@app.route('/healthcheck.json')
def healthcheck():
    return no_cache(Response(
        '{"*": {"status": true}}',
        content_type='application/json',
    ))


def no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response
