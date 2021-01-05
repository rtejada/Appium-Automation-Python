from appium import webdriver
desired_cap = {

      "platformName": "Android",
      "platformVersion": "9",
      "deviceName": "star2lte",
      "automationName": "UiAutomator1",
      "appPackage": "com.sec.android.app.samsungapps",
      "appActivity": "com.sec.android.app.samsungapps.SamsungAppsMainActivity"
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.find_element_by_id('com.sec.android.app.samsungapps:id/isa_accept_terms_and_conditions').click()
driver.find_element_by_id('com.sec.android.app.samsungapps:id/btn_welcome_legal_info_agree').click()
driver.find_element_by_id('com.sec.android.app.samsungapps:id/actionbar_search_icon').click()
driver.find_element_by_id('android:id/search_src_text').send_keys('samsung')
driver.execute_script('mobile: performEditorAction', {'action': 'search'})

'''
popBtn = driver.find_element_by_id('com.sec.android.app.samsungapps:id/actionbar_search_icon')
driver.set_value(popBtn, 'NOT NOW')
'''