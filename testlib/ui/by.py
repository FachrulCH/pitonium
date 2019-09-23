from appium.webdriver.common.mobileby import MobileBy
from selene.support import by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expecting

import configs
from . import application

def platform_locator(selectors):
	return selectors.get(configs.devices.PLATFORM, 'Undefined Platform Selector')


def accessibility_id(_id):
	return MobileBy.ACCESSIBILITY_ID, _id

def id(_id):
	return MobileBy.ID, _id

# def _id(id_name):
# 	return WebDriverWait(application.instance, 5).until(
# 		expecting.visibility_of_element_located((
# 		MobileBy.ID, id_name)))

css = by.css
xpath = by.xpath
# id = _id
