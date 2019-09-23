from selene.conditions import visible
from testlib.ui.screens import home_screen
from testlib.ui.screens import explorer_screen
from time import sleep


def test_searching(app):
	home_screen.btn_explore.click()
	explorer_screen.input_search.click()
	explorer_screen.input_search.should_be(visible)
	explorer_screen.input_search.send_keys('#Bekasi')
	sleep(3)
	print('Result should show')
	# breakpoint()