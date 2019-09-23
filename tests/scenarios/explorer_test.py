from selene.conditions import visible
from selene.support.conditions import have
from grappa import expect

from testlib.ui.screens import home_screen
from testlib.ui.screens import explorer_screen
from testlib.ui.screens import profile_screen
from time import sleep


def test_searching_person_and_follow(app):
	home_screen.btn_explore.click()
	explorer_screen.input_search.click()
	explorer_screen.input_search.should_be(visible)
	explorer_screen.input_search.send_keys('fachrulch')
	print('Result should show')
	explorer_screen.list_result_person.first().click()
	# breakpoint()
	expect(profile_screen.text_profile_title.text).to.equal('fachrulch')
	if profile_screen.btn_follow.text == 'Following':
		print('I followed you already')
	else:
		print('OK i will follow you')
		profile_screen.btn_follow.click()



def test_searching_hashtag(app):
	home_screen.btn_explore.click()
	explorer_screen.input_search.click()
	explorer_screen.input_search.should_be(visible)
	explorer_screen.input_search.send_keys('#Jakarta')
	print('Result should show')
	explorer_screen.list_result_hashtag.first().click()
