from appium_test1.xueqiu_po.page.base_page import BasePage
from appium_test1.xueqiu_po.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
