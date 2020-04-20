from appium.webdriver.common.mobileby import MobileBy

from appium_test1.three.page.base_page import BasePage
from appium_test1.three.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    def click_addmember(self):
        # 滚动查找  添加成员
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable('

                                                'new UiSelector().scrollable(true).instance(0))'

                                                '.scrollIntoView(new UiSelector().text("添加成员")'

                                                '.instance(0));').click()
        return MemberInvitePage(self._driver)
