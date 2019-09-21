from selene.support.jquery_style_selectors import s, ss
import configs

def locator_for_platform(selectors):
	return selectors.get(configs.devices.PLATFORM, 'Undefined Selector')

def element(selectors):
	return s(locator_for_platform(selectors))

def elements(selectors):
	return ss(locator_for_platform(selectors))