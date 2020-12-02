import pytest

import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:

        yield client



def test_home_page(client):
    rv = client.get('/')
    assert b'Wellcome' in rv.data

def test_school_word(client):
    rv = client.get('/words/school')
    assert b'okul' in rv.data

def test_blank(client):
    rv = client.get('/words/  ')
    assert b'Invalid' in rv.data

def test_useless_word(client):
    rv = client.get('/words/adsfasdf')
    assert b'No such' in rv.data