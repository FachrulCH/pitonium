from .. import by, ui

input_search = ui.element({
	'ANDROID': by.xpath('//android.widget.EditText[@resource-id="com.instagram.android:id/action_bar_search_edit_text"]'),
	'IOS': by.xpath('')
})

list_result = ui.elements({
	'ANDROID': by.xpath('//android.widget.FrameLayout[@resource-id="com.instagram.android:id/row_hashtag_container"]'),
	'IOS': by.xpath('')
})