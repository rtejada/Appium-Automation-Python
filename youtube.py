from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




def capabilities():
    desired_cap = {}
    desired_cap["platformName"] = "Android"
    desired_cap["platformVersion"] = "9"
    desired_cap["deviceName"] = "star2lte"
    desired_cap["automationName"] = "UiAutomator1"
    desired_cap["appPackage"] = "com.google.android.youtube"
    desired_cap["appActivity"] = "com.google.android.apps.youtube.app.WatchWhileActivity"
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

driver = capabilities()
text = 'Ivan Tay Selenium Automation'
ENTER = 66
SEARCH = 'com.google.android.youtube:id/search_edit_text'
XPATH1 = '//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.youtube:id/results"]/android.view.ViewGroup'
driver.find_element_by_accessibility_id('Buscar').click()

try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, SEARCH)))
except TimeoutException:
    print('Time out. Cannot find list in here')
    driver.quit()
driver.find_element_by_id('com.google.android.youtube:id/search_edit_text').send_keys(text)
driver.press_keycode(ENTER)



try:
    elements = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH1)))
except TimeoutException:
    print('Time out. Cannot find list in here')
    driver.quit()

element = driver.find_elements_by_xpath(XPATH1)
for i in element:
    print(i)
element[2].click()