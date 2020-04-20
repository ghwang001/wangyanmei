from appium_test1.xueqiu_po.page.base_page import BasePage
from appium_test1.xueqiu_po.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)
