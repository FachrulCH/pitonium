import pytest
from selene import factory


from testlib.ui import driver, application


@pytest.fixture(scope='session')
def app():
	mobile_driver = driver.get()
	factory.set_shared_driver(mobile_driver)

	yield application

	driver.close(mobile_driver)
