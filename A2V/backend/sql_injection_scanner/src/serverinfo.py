import time
import signal
import multiprocessing
import bs4
from urllib.parse import urlparse

from src import std
from src.web import web

def init():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def check(urls):
    """Get server information of multiple domains with multiprocessing"""

    domains_info = []  # Return in list for termtable input
    results = {}  # Store results

    childs = []  # Store child processes
    max_processes = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(max_processes, init)

    for url in urls:
        def callback(result, url=url):
            results[url] = result
        childs.append(pool.apply_async(__getserverinfo, (url, ), callback=callback))

    try:
        while True:
            time.sleep(0.5)
            if all([child.ready() for child in childs]):
                break
    except KeyboardInterrupt:
        std.stderr("Skipping server info scanning process")
        pool.terminate()
        pool.join()
    else:
        pool.close()
        pool.join()

    # If the user skipped the process, some may not have information
    # So put '-' for empty data
    for url in urls:
        if url in results.keys():
            data = results.get(url)
            domains_info.append([url, data[0], data[1]])
            continue

        domains_info.append([url, '', ''])

    return domains_info

def __getserverinfo(url):
    """Get server name and version of the given domain"""

    url = urlparse(url).netloc if urlparse(url).netloc != '' else urlparse(url).path.split("/")[0]

    info = []  # To store server info
    url = "https://aruljohn.com/webserver/" + url

    try:
        result = web.gethtml(url)
    except KeyboardInterrupt:
        raise KeyboardInterrupt

    try:
        soup = bs4.BeautifulSoup(result, "html.parser")
    except:
        return ['', '']

    if soup.findAll('p', {"class" : "err"}):
        return ['', '']

    for row in soup.findAll('tr'):
        if row.findAll('td', {"class": "title"}):
            info.append(row.findAll('td')[1].text.rstrip('\r'))

    return info
