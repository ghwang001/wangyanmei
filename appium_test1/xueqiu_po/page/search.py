from appium_test1.xueqiu_po.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        # 定义命中规则,命中yaml文件中的{value}值
        self._params["value"] = value
        self.steps("../page/search.yaml")
