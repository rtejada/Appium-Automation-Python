from appium import webdriver


def calculadora():

    desired_cap = {

      "platformName": "Android",
      "platformVersion": "9",
      "deviceName": "star2lte",
      "automationName": "UiAutomator1",
      "appPackage": "com.google.android.calculator",
      "appActivity": "com.android.calculator2.Calculator"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

    return driver
