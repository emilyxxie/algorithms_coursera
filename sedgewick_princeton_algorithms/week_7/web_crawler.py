'''

Use BFS to implement a simple webcrawler.
Make a directed graph from crawl.



# TODO: finish this later. I get the point.

'''

from directed_graph import DirectedGraph
import urllib

class WebCrawler(object):

  def __init__(self):
    self.queue = []
    self.digraph = DirectedGraph()

  def crawl(self, site):
    self.queue.append(site)
    while self.queue:
      url = self.queue.pop()
      self.__scrape(url)


    if len(self.digraph.vertices) > 10:
      return

  # scrapes site for urls.
  def __scrape(self, url):
    site = urllib.urlopen(url)
    contents = site.read()
    # only accounting for http, https, or www
    # excluding relative URLs for now
    regex = '<a href="(www.*?|https?://.*?)"'
    # url = "http://wikipedia.com"
    # site = urllib.urlopen(url)

# print site.reaxd()


  def clear(self):
    self.queue = []


crawler = WebCrawler()
crawler.crawl("https://en.wikipedia.org/wiki/Code")

print(crawler)
