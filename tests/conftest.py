import pytest


@pytest.fixture(scope='function')
def setup():
    yield
    print("test is finished")
