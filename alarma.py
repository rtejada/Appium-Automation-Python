from appium import webdriver


def alarma():

    driver = {

      "platformName": "Android",
      "platformVersion": "9",
      "deviceName": "star2lte",
      "automationName": "UiAutomator1",
      "appPackage": "com.sec.android.app.clockpackage",
      "appActivity": "com.sec.android.app.clockpackage.ClockPackage"
    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    return driver
