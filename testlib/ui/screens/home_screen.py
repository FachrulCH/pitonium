from .. import by, ui

btn_explore  = ui.element({
	'ANDROID': by.xpath('//android.widget.LinearLayout[@resource-id="com.instagram.android:id/tab_bar"]/android.widget.FrameLayout[2]'),
	'IOS': ''
})

btn_home = ui.element({
	'ANDROID': by.xpath('//android.widget.LinearLayout[@resource-id="com.instagram.android:id/tab_bar"]/android.widget.FrameLayout[1]'),
	'IOS': ''
})