# 匯入webdriver
from appium import webdriver

# 初始化引數
desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["appium:platformVersion"] = "12"
desired_caps["appium:deviceName"] = "RF8R50PA33R"
desired_caps["appium:appPackage"] = "com.android.chrome"
desired_caps["appium:appActivity"] = "com.google.android.apps.chrome.Main"
desired_caps["newCommandTimeout"] = 100000

# 連線Appium Server，初始化自動化環境
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 設定等待時間，如果不給時間的話可能會找不到元素
driver.implicitly_wait(5)