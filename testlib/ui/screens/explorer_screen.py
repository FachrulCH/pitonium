from .. import by, ui

input_search_xpath = ui.element({
	'ANDROID': by.xpath('//android.widget.EditText[@resource-id="com.instagram.android:id/action_bar_search_edit_text"]'),
	'IOS': by.xpath('')
})

input_search = ui.element({
	'ANDROID': by.id('action_bar_search_edit_text'),
	'IOS': by.xpath('')
})

list_result_xpath = ui.elements({
	'ANDROID': by.xpath('//android.widget.FrameLayout[@resource-id="com.instagram.android:id/row_hashtag_container"]'),
	'IOS': by.xpath('')
})

list_result_hashtag = ui.elements({
	'ANDROID': by.id('row_hashtag_container'),
	'IOS': by.xpath('')
})
list_result_person = ui.elements({
	'ANDROID': by.id('row_search_user_info_container'),
	'IOS': by.xpath('')
})

