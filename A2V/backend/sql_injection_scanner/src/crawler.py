import re
from urllib.parse import urlparse

from nyawc.Options import Options
from nyawc.QueueItem import QueueItem
from nyawc.Crawler import Crawler as nyawcCrawler
from nyawc.CrawlerActions import CrawlerActions
from nyawc.http.Request import Request


class Crawler:
    def __init__(self):
        self.links = []
        self.crawler = None
        self.setoptions()

    def crawl(self, url):
        if self.crawler is None:
            print("Crawler is not set up")
            return

        parsed_url = urlparse(url)
        domain = parsed_url.scheme + "://" + parsed_url.netloc

        self.links = []
        self.crawler.start_with(Request(domain))
        return self.links

    def setoptions(self, depth=1):
        

        options = Options()
        options.scope.max_depth = depth
        options.callbacks.crawler_before_start = self.crawlerstart
        options.callbacks.crawler_after_finish = self.crawlerfinish
        options.callbacks.request_before_start = self.requeststart
        options.callbacks.request_after_finish = self.requestfinish

        self.crawler = nyawcCrawler(options)

    def crawlerstart(self):
        # Called before the crawler starts crawling. Default is a null route.
        pass

    def crawlerfinish(self, queue):
        # Called after the crawler finished crawling. Default is a null route.
        pass

    def requeststart(self, queue, queue_item):
        # Called before the crawler starts a new request. Default is a null route.
        return CrawlerActions.DO_CONTINUE_CRAWLING

    def requestfinish(self, queue, queue_item, new_queue_items):
        # Called after the crawler finishes a request. Default is a null route.
        url = queue_item.request.url
        if re.search('(.*?)(.php\?|.asp\?|.apsx\?|.jsp\?)(.*?)=(.*?)', url):
            if url not in self.links:
                self.links.append(url)
        return CrawlerActions.DO_CONTINUE_CRAWLING
