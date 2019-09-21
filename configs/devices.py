import os
from selene import config as _selene_config
from . import env

_selene_config.timeout = int(env.get('UI_TIMEOUT', 30))
APPIUM_TIMEOUT = int(env.get('APPIUM_TIMEOUT', 3600))

APPIUM_SERVER = env.get('APPIUM_SERVER', 'http://0.0.0.0:4723/wd/hub')
PLATFORM = env.get('PLATFORM', 'ANDROID')
IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'

APP_NAME = {
    'IOS': env.get('IOS_APP_NAME', 'some_cool.app'),
    'ANDROID': env.get('ANDROID_APP_NAME', 'need_some_cool.apk')
}.get(PLATFORM)

_DEFAULT_APP_PATH = str(os.path.join(os.getcwd(), fr"app/{APP_NAME}"))
MOBILE_APP = env.get('MOBILE_APP', _DEFAULT_APP_PATH)

ANDROID_VERSION = env.get('ANDROID_VERSION', '7.0')
ANDROID_DEVICE_NAME = env.get('ANDROID_DEVICE_NAME', 'Pixel_3a_API_24')
ANDROID_APP_PACKAGE = env.get('ANDROID_APP_PACKAGE', 'com.instagram.android')
ANDROID_APP_ACTIVITY = env.get('ANDROID_APP_ACTIVITY', 'com.instagram.android.activity.MainTabActivity')

IOS_VERSION = env.get('IOS_VERSION', '11.4')
IOS_DEVICE_NAME = env.get('IOS_DEVICE_NAME', 'iPhone X')