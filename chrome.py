from appium import webdriver
desired_cap = {

      "platformName": "Android",
      "platformVersion": "9",
      "deviceName": "star2lte",
      "automationName": "UiAutomator1",
      "appPackage": "com.android.chrome",
      "appActivity": "com.google.android.apps.chrome.Main"
    }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.find_element_by_id('com.android.chrome:id/terms_accept').click()
driver.find_element_by_id('com.android.chrome:id/positive_button').click()
driver.find_element_by_id('com.android.chrome:id/search_box_text').send_keys('flipkart')
