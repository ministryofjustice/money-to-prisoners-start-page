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
        content_type='text/plain'
    )
