import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from src.web import useragents


def gethtml(url, lastURL=False):
    """Return HTML of the given URL"""

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    header = useragents.get()
    request = urllib.request.Request(url, headers=header)
    html = None

    try:
        with urllib.request.urlopen(request, timeout=10) as reply:
            html = reply.read().decode('utf-8')

    except HTTPError as e:
        # Read HTML content anyway for reply with HTTP 500
        if e.code == 500:
            html = e.read().decode('utf-8')
        # print("[{}] HTTP error".format(e.code))

    except URLError as e:
        # print("URL error, {}".format(e.reason))
        pass

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except Exception as e:
        # print("HTTP exception:", e)
        pass

    if html:
        if lastURL:
            return (html, reply.geturl())
        else:
            return html

    return False
