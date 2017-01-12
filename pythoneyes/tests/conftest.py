import pytest

from pythoneyes.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    setup our flask test app, esto se ejecuta solo una vez

    :return: Flask app
    """

    params = {
            'DEBUG': False,
            'TESTING': True
            }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    '''
    Setup an app client, this get executed for each test function

    :param app: Pytest fixture
    :return: Flask app client
    '''
    yield app.test_client()
