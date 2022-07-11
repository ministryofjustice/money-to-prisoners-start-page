def test_start_page(client, settings):
    response = client.get('/')
    assert response.status_code == 200, 'Should get a 200 status'
    assert 'You can use this service to make a payment by Visa, Mastercard or Maestro debit card' in response.text, \
        'Should mention card options'
    assert f'href="{settings.SEND_MONEY_URL}"' in response.text, 'Should link to send-money app'
    assert 'href="/info"' in response.text, 'Should link to info page'


def test_info_page(client):
    response = client.get('/info')
    assert response.status_code == 200, 'Should get a 200 status'
    assert 'The money is paid into the prisoner’s account' in response.text, \
        'Should mention prisoner account'


def test_metrics(client, settings):
    response = client.get('/metrics')
    assert response.status_code == 401, 'Should require basic auth'
    assert 'mtp_app_info' not in response.text, 'Should not include metrics when unauthorised'

    response = client.get('/metrics', auth=(settings.METRICS_USER, settings.METRICS_PASS))
    assert response.status_code == 200, 'Should permit basic auth'
    assert 'mtp_app_info{' in response.text, 'Should include mtp app info metric'


def test_404(client):
    response = client.get('/not-found')
    assert response.status_code == 404, 'Should get a 404 status'
