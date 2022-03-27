import requests
from decouple import config
APP_URL = config("APP_URL")

def test_healthcheck():
    response = requests.get(APP_URL+'ping')
    assert response.status_code == 200, 'Healthcheck not passed'

def test_emma_output():
    response = requests.get(APP_URL+"credit-data/424-11-9327")
    assert response.status_code == 200, "App has not send successful request for first test-person's data"
    assert response.json() == {
        'address': '9493 Westend Terrace',
        'assessed_income': 60668,
        'balance_of_debt': 11585,
        'complaints': True,
        'first_name': 'Emma',
        'last_name': 'Gautrey'
    }, 'Data for first-test-person (with ssn = 424-11-9327) was not aggregated correctly'

def test_billy_output():
    response = requests.get(APP_URL+"credit-data/553-25-8346")
    assert response.status_code == 200, "App has not send successful request for second test-person's data"
    assert response.json() == {
        'address': '2911 Providence Lane La Puente, CA 91744',
        'assessed_income': 89437,
        'balance_of_debt': 178,
        'complaints': False,
        'first_name': 'Billy',
        'last_name': 'Brinegar'
    }, 'Data for second test-person (with ssn = 553-25-8346) was not aggregated correctly'

def test_gail_output():
    response = requests.get(APP_URL+"credit-data/287-54-7823")
    assert response.status_code == 200, "App has not send successful request for second test-person's data"
    assert response.json() == {
        'address': '7619 Rainbow Drive Canton, OH 44702',
        'assessed_income': 42301,
        'balance_of_debt': 23087,
        'complaints': True,
        'first_name': 'Gail',
        'last_name': 'Shick'
    }, 'Data for third test-person (with ssn = 287-54-7823) was not aggregated correctly'

def test_non_existing_ssn():
    response = requests.get(APP_URL+"credit-data/some_trash")
    assert response.status_code == 404, "App can not handle requests for not-existing targets properly"
