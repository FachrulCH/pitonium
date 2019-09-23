# Pitonium 🐍

Simplify automation framework for Mobile using Appium and python
Inspired by: https://github.com/ibalagurov/heisenbug_piter_2018_example



## Precondition

- Installed Python 3.7
- Installed Appium server
- Installed all appium depedencies

## Install Depedencies

`pip3 install pipenv`
`pipenv install`

## Running Test
make sure appium server is up and running:
run in console: `appium --log-level warn:debug`

`PLATFORM=ANDROID pipenv run pytest tests/ui/`
`PLATFORM=IOS pipenv run pytest tests/ui/`

Specific test to run
`pipenv run pytest -s tests/scenarios/explorer_test.py::test_searching_person_and_follow`

## Technology used
- Pytest : Test runner
- Selene : Wrapper selenium / appium with good DSL
- Appium : Automation library for mobile
- Grappa : Cool assertion for readable test writes assert/expect

## Demo test running
![Pitonium is running](./pitonium-demo.gif "Test running")

