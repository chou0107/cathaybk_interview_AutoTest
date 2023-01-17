from InitAppium import *
from Variables import *
from Selectors import *

from appium.webdriver.common.appiumby import AppiumBy
import time

#點擊"接受並繼續"按鈕
driver.find_element(by=AppiumBy.ID, value=AcceptButton).click()

#點擊"不用了，謝謝"按鈕
driver.find_element(by=AppiumBy.ID, value=NoThanksButton).click()

#於搜尋輸入框欄位輸入網址並進行搜尋
driver.find_element(by=AppiumBy.ID, value=SearchTextfield).send_keys(SearchItem)
driver.find_element(by=AppiumBy.XPATH, value=SearchResult).click()

#截圖
#WebDriverWait(driver, time_out).until(lambda driver: driver.find_element(*id))
#WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, Page)))
time.sleep(20)
driver.save_screenshot("screenshot1.png")

#點擊左上漢堡選單
time.sleep(20)
driver.find_element(by=AppiumBy.XPATH, value=HamburgerIcon).click()

#點擊"產品介紹"
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH, value=ProductIntroduceButton).click()

#點擊"信用卡"
time.sleep(5)
driver.find_element(by=AppiumBy.XPATH, value=CreditCardButton).click()

