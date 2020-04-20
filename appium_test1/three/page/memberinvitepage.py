from appium.webdriver.common.mobileby import MobileBy

from appium_test1.three.page.base_page import BasePage


class MemberInvitePage(BasePage):
    def click_menualadd(self):
        from appium_test1.three.page.contactaddpage import ContactAddPage
        # 手动添加
        self.find(MobileBy.ID, "com.tencent.wework:id/c56").click()
        return ContactAddPage(self._driver)

    def click_back(self):
        from appium_test1.three.page.addresslistpage import AddressListPage
        return AddressListPage(self._driver)

    def veriy_toast(self):
        self.find(MobileBy.XPATH, "//*[contains(@text,'添加成功')]")
        return self
