from appium import webdriver as appium_driver
from configs import devices

# 'app': devices.MOBILE_APP,

_capabilities = {
	'ANDROID': {
		'platformName': 'Android',
		'platformVersion': devices.ANDROID_VERSION,
		'deviceName': devices.ANDROID_DEVICE_NAME,
		'noReset': True,
		'newCommandTimeout': devices.APPIUM_TIMEOUT,
		'automationName': 'UiAutomator2',
		'appPackage': devices.ANDROID_APP_PACKAGE,
		'appActivity': devices.ANDROID_APP_ACTIVITY,
		'browserName': ''
	},
	'IOS': {
		'version': '',
		'platformName': '',
		'platformVersion': '',
		'deviceName': '',
		'app': '',
		'noReset': '',
		'fullReset': '',
		'newCommandTimeout': ''
	}
}


def get():
	caps = _capabilities[devices.PLATFORM]
	return appium_driver.Remote(
		command_executor=devices.APPIUM_SERVER,
		desired_capabilities=caps
	)


def close(driver):
	driver.close_app()
