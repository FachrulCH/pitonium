#!/usr/bin/env bash

export PLATFORM=ANDROID
rm -rf report
mkdir -p report
#python3 -m pytest tests/scenarios/ -l -vv --tb=short
pipenv run pytest -s tests/scenarios/ --alluredir report/

#generate report
#allure serve report