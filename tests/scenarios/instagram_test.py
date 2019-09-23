from testlib.ui.screens import home_screen
from time import sleep

def test_pertamax(app):
	print('Runnning first test')
	home_screen.btn_explore.click()
	home_screen.btn_home.click()
	sleep(3)
	print('Calling general method')
	app.mondar_mandir()

def test_keduax(app):
	print('\n ==============')
	print('\n Runnning Second test')
	home_screen.btn_explore.click()
	home_screen.btn_home.click()
	sleep(3)
	print('Calling general method')
	app.mondar_mandir()
