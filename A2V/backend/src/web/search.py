import sys
from urllib.request import HTTPError, URLError
from lib import bing
from lib import google
from lib import yahoo

bingsearch = bing.Bing()
yahoosearch = yahoo.Yahoo()

class Search:
    """Basic search class that can be inherited by other search agents like Google, Yandex"""
    pass

class Google(Search):
    def search(self, query, pages=10):
        """Search and return an array of URLs"""

        urls = []

        try:
            for url in google.search(query, start=0, stop=pages):
                urls.append(url)
        except HTTPError:
            sys.exit("[503] Service Unreachable")
        except URLError:
            sys.exit("[504] Gateway Timeout")
        except Exception as e:
            sys.exit(f"Unknown error occurred: {e}")
        else:
            return urls

class Bing(Search):
    def search(self, query, pages=10):
        try:
            return bingsearch.search(query, stop=pages)
        except HTTPError:
            sys.exit("[503] Service Unreachable")
        except URLError:
            sys.exit("[504] Gateway Timeout")
        except Exception as e:
            sys.exit(f"Unknown error occurred: {e}")

class Yahoo(Search):
    def search(self, query, pages=1):
        try:
            return yahoosearch.search(query, pages)
        except HTTPError:
            sys.exit("[503] Service Unreachable")
        except URLError:
            sys.exit("[504] Gateway Timeout")
        except Exception as e:
            sys.exit(f"Unknown error occurred: {e}")
