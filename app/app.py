from flask import Flask, Response, redirect, render_template, request
from prometheus_client import exposition
from prometheus_client.metrics_core import InfoMetricFamily
from prometheus_client.registry import CollectorRegistry

import settings


class AppMetricCollector:
    def __init__(self):
        self.info = InfoMetricFamily('mtp_app', 'Details of a money-to-prisoners app', value=dict(
            app=settings.APP,
            environment=settings.ENVIRONMENT,
            git_commit=settings.APP_GIT_COMMIT,
            build_tag=settings.APP_BUILD_TAG,
            build_date=settings.APP_BUILD_DATE,
        ))

    def collect(self):
        return [self.info]


metric_registry = CollectorRegistry()
metric_registry.register(AppMetricCollector())

app = Flask(__name__)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
)


@app.route('/')
def index():
    if settings.ENVIRONMENT == 'prod':
        return redirect('https://www.gov.uk/send-prisoner-money')
    return render_template('index.html', **settings.TEMPLATE_CONTEXT)


@app.route('/info')
def info():
    if settings.ENVIRONMENT == 'prod':
        return redirect('https://www.gov.uk/staying-in-touch-with-someone-in-prison')
    return render_template('info.html', **settings.TEMPLATE_CONTEXT)


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
        settings.PING_JSON,
        content_type='application/json',
    ))


@app.route('/healthcheck.json')
def healthcheck():
    return no_cache(Response(
        '{"*": {"status": true}}',
        content_type='application/json',
    ))


@app.route('/metrics')
def metrics():
    auth = request.authorization
    if not auth or auth.username != settings.METRICS_USER or auth.password != settings.METRICS_PASS:
        return Response('Auth required', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    encoder, content_type = exposition.choose_encoder(request.headers.get('Accept'))
    return no_cache(Response(
        encoder(metric_registry),
        content_type=content_type,
    ))


def no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response
