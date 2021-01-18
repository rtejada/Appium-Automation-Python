from alarma import *
from appium.webdriver.common.touch_action import TouchAction

driver = alarma()

'''
Touch Actions
(new TouchAction(driver))
  .press({x: 357, y: 709})
  .moveTo({x: 362: y: 188})
  .release()
  .perform()
  

'''
touch = TouchAction(driver)
touch.press(x=357, y=709).move_to(x=362, y=188).release().perform()


driver.find_element_by_id("com.sec.android.app.clockpackage:id/menu_alarm_add").click()
for i in range(0, 5):
    driver.find_element_by_id("com.sec.android.app.clockpackage:id/repeat_"+str(i)).click()

driver.find_element_by_id("com.sec.android.app.clockpackage:id/alarm_name").send_keys('Roxana')
driver.find_element_by_id("com.sec.android.app.clockpackage:id/smallLabel").click()




