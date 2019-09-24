#!/usr/bin/env bash

export PLATFORM=ANDROID

rm -rf report
mkdir -p report
#python3 -m pytest tests/scenarios/ -l -vv --tb=short
#pipenv run pytest -s tests/scenarios/explorer_test.py --alluredir report/
ANDROID_VERSION="7.0" ANDROID_DEVICE_NAME="emulator-5554" APPIUM_SERVER="http://0.0.0.0:4723/wd/hub" pipenv run pytest -s tests/scenarios/explorer_test.py &
ANDROID_VERSION="9" ANDROID_DEVICE_NAME="emulator-5556" APPIUM_SERVER="http://0.0.0.0:4724/wd/hub" pipenv run pytest -s tests/scenarios/instagram_test.py
#generate report
#allure serve report