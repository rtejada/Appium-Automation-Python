from alarma import *

driver = alarma()

driver.find_element_by_id("com.sec.android.app.clockpackage:id/menu_alarm_add").click()
for i in range(0, 5):
    driver.find_element_by_id("com.sec.android.app.clockpackage:id/repeat_"+str(i)).click()

driver.find_element_by_id("com.sec.android.app.clockpackage:id/alarm_name").send_keys('Roxana')
driver.find_element_by_id("com.sec.android.app.clockpackage:id/smallLabel").click()




