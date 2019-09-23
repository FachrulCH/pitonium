from .. import by, ui

text_profile_title  = ui.element({
	'ANDROID': by.id('action_bar_textview_title'),
	'IOS': ''
})

list_actions = ui.elements({
	'ANDROID': by.id('profile_header_actions_top_row'),
	'IOS': ''
})

btn_follow = ui.element({
	'ANDROID': by.xpath('//android.widget.LinearLayout[@resource-id="com.instagram.android:id/profile_header_actions_top_row"]/android.widget.TextView'),
	'IOS': ''
})