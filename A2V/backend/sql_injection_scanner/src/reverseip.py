import sys
import urllib.request
import urllib.parse
import json
from urllib.parse import urlparse
from src.web import useragents  

def reverseip(url):
    """Return domains from the given server"""

    # Get only domain name
    parsed_url = urlparse(url)
    url = parsed_url.netloc if parsed_url.netloc != '' else parsed_url.path.split("/")[0]

    source = "http://domains.yougetsignal.com/domains.php"
    user_agent = useragent.get()
    content_type = "application/x-www-form-urlencoded; charset=UTF-8"

    # POST method
    data = urllib.parse.urlencode({'remoteAddress': url, 'key': ''}).encode()
    request = urllib.request.Request(source, data)
    request.add_header("Content-Type", content_type)
    request.add_header("User-Agent", user_agent)

    try:
        result = urllib.request.urlopen(request).read().decode()

    except urllib.error.HTTPError as e:
        print(f"[{e.code}] HTTP error", file=sys.stderr)
        return []

    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}", file=sys.stderr)
        return []

    except Exception as e:
        print(f"HTTP exception: {e}", file=sys.stderr)
        return []

    obj = json.loads(result)

    # If successful
    if obj["status"] == 'Success':
        return [domain[0] for domain in obj["domainArray"]]

    print(f"[ERR] {obj['message']}", file=sys.stderr)
    return []

