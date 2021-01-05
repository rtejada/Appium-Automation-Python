from calculadora import *

driver = calculadora()

#suma

driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()

#multiplicacion

driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
driver.find_element_by_id("com.google.android.calculator:id/op_mul").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()

#division

driver.find_element_by_id("com.google.android.calculator:id/digit_8").click()
driver.find_element_by_id("com.google.android.calculator:id/op_div").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()