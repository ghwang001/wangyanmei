from appium import webdriver

from appium_test1.xueqiu_po.page.base_page import BasePage
from appium_test1.xueqiu_po.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            # 启动 app
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['autoGranPermissions'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
