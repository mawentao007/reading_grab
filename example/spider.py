# coding:utf-8
# crawl github project list

from grab import Grab
import logging

logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.go('https://github.com/login')
print g.doc.form
g.doc.set_input('login', '1812@qq.com')
g.doc.set_input('password', '')
g.doc.submit()
g.doc.save('/tmp/x.html')


home_url = g.doc('//a[contains(@class, "header-nav-link name")]/@href').text()
repo_url = home_url + '?tab=repositories'

g.go(repo_url)
for elem in g.doc.select('//h3[@class="repo-list-name"]/a'):
    print('%s: %s' % (elem.text(),
                      g.make_url_absolute(elem.attr('href'))))




# from grab.spider import Spider, Task
# import logging
#
# class ExampleSpider(Spider):
#     def task_generator(self):
#         for lang in ('python', 'ruby', 'perl'):
#             url = 'https://www.google.com/search?q=%s' % lang
#             yield Task('search', url=url, lang=lang)
#
#     def task_search(self, grab, task):
#         print('%s: %s' % (task.lang,
#                           grab.doc('//div[@class="s"]//cite').text()))
#
#
# logging.basicConfig(level=logging.DEBUG)
# bot = ExampleSpider()
# bot.run()
