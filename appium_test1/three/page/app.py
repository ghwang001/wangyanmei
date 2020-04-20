from appium import webdriver

from appium_test1.three.page.base_page import BasePage
from appium_test1.three.page.main import Main


class App(BasePage):
    # 启动 app
    def start(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = True
        caps['automationName'] = 'uiautomator2'
        # caps['unicodeKeyBoard'] = True
        # caps['resetKeyBoard'] = True
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self._driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
