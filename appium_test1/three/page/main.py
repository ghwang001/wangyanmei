from appium.webdriver.common.mobileby import MobileBy

from appium_test1.three.page.addresslistpage import AddressListPage
from appium_test1.three.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        # self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.steps("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass

    def goto_profilr(self):
        pass
