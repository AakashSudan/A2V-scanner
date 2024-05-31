import argparse
from urllib.parse import urlparse

from src import std
from src import scanner
from src import serverinfo
from src.crawler import Crawler

# crawler instance
crawler = Crawler()

def singlescan(url):
    """Instance to scan single targeted domain."""
    if urlparse(url).query != '':
        result = scanner.scan([url])
        if result:
            # scanner.scan prints if vulnerable
            return result
        else:
            print("")  # move carriage return to newline
            std.stdout("No SQL injection vulnerability found")
            option = std.stdin("Do you want to crawl and continue scanning? [Y/N]", ["Y", "N"], upper=True)
            if option == 'N':
                return False

    # Crawl and scan the links
    std.stdout("Going to crawl {}".format(url))
    urls = crawler.crawl(url)
    if not urls:
        std.stdout("Found no suitable URLs to test SQLi")
        return False

    std.stdout("Found {} URLs from crawling".format(len(urls)))
    vulnerables = scanner.scan(urls)
    if not vulnerables:
        std.stdout("No SQL injection vulnerability found")
        return False

    return vulnerables

def initparser():
    """Initialize parser arguments."""
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="target", help="Scan target website", type=str, required=True, metavar="www.example.com")

if __name__ == "__main__":
    initparser()
    args = parser.parse_args()

    if args.target:
        vulnerables = singlescan(args.target)
        if not vulnerables:
            exit(0)

        # Show domain information of target URLs
        std.stdout("Getting server info of domains can take a few minutes")
        table_data = serverinfo.check([args.target])
        std.printserverinfo(table_data)
        print("")  # give space between two tables
        std.normalprint(vulnerables)
        exit(0)
    else:
        parser.print_help()
