import unittest
import HTMLTestRunner
import os
import time
#search方法
class Search():
    def search(self):
        print("search方法")
class TestDemo(unittest.TestCase):
    #在每个方法的前执行
    def setUp(self) -> None:
        print("setup")
    #在每个方法的后执行
    def tearDown(self) -> None:
        print("tearDown")

    def test_search(self):
        print("search11111111111")
        search = Search()
        search.search()
    def test_search1(self):
        print("search2222222222")
        search = Search()
        search.search()

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(TestDemo("test_search"))
    suit.addTest(TestDemo("test_search1"))
    # unittest.TextTestRunner().run(suit)
    report_path = os.path.join(os.path.dirname(__file__),'report')
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename = report_path+"/"+now+"_result.html"
    fname1 = "wode.html"
    with open(filename,'wb')as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="MyReport", description='测试一下哈')
        runner.run(suit)