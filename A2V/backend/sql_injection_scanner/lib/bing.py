
__name__    = 'python-bing'
__version__ = "0.0.1"

import re
import urllib.parse
import urllib.request

class Bing:
    def __init__(self):
        self.bingsearch = "http://www.bing.com/search?%s"
        self.regex = re.compile(r'<h2><a href="(.*?)"')

    def default_headers(self, name=__name__):
        '''
        :type name : str
        :param name: Name to add user-agent 

        :rtype: dict
        '''

        return {
            'Accept'         : 'text/html',
            'Connection'     : 'close',
            'User-Agent'     : '%s/%s' % (name, __version__),
            'Accept-Encoding': 'identity'
            }

    def get_page(self, URL):
        '''
        :type URL : str
        :param URL: URL to get HTML source 

        :rtype: str
        '''

        request = urllib.request.Request(URL, headers=self.default_headers())
        resp = urllib.request.urlopen(request)

        return resp.read().decode('utf-8')

    def parse_links(self, html):
        '''
        :type html : str
        :param html: HTML source to find links

        :rtype: list
        '''

        return re.findall(self.regex, html)

    def search(self, query, stop=100):
        '''
        :type query : str
        :param query: Query for search
        
        :type stop  : int
        :param stop : Last result to retrieve.

        :rtype: list
        '''
 
        links = []
        start = 1

        for page in range(int(stop) // 10):
            URL = (self.bingsearch % (urllib.parse.urlencode({'q': query}))) + '&first=' + str(start)

            html = self.get_page(URL)
            result = self.parse_links(html)

            [links.append(_) for _ in result if _ not in links]

            start = start + 10

        return links
