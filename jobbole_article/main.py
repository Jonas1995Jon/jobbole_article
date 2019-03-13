import re

from scrapy import cmdline

cmdline.execute("scrapy crawl jobbole".split())

# class Test(object):
#     def test(self):
#         str = " 2 评论"
#         reg = '.*(\d+).*'
#         str_reg = re.match(reg, str)
#         print(str_reg.group(1))
# if __name__ == '__main__':
#     test = Test()
#     test.test()