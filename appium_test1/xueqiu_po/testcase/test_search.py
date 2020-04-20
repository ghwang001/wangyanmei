from appium_test1.xueqiu_po.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
