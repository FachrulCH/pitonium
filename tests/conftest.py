import pytest
from selene import factory


from testlib.ui import driver, application


# @pytest.fixture(scope='session')
@pytest.fixture
def app():
	print("\n==> Setup up App driver")
	mobile_driver = driver.get()
	factory.set_shared_driver(mobile_driver)

	yield application

	print("\n==> Closing down App driver")
	driver.close(mobile_driver)
