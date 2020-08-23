import argparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

parser = argparse.ArgumentParser(description='Simple Web Crawler')
parser.add_argument('-u', '--url', metavar='', default='https://mix.com',
                    type=str, help='Seed URL for crawling')
args = parser.parse_args()

URLS_TO_CRAWL = []
PARENT_LINK = {}

def is_url_valid(link):
    if not link or any(ext in link for ext in ('.pdf', 'docx')) \
            or link.startswith('mailto:'):
        return False
    else:
        return True

def getWebsiteAssets(url):
    links, image_sources = fetch(url)
    print(links)
    print(image_sources)
    if (len(PARENT_LINK.keys()) == 2):
        return
    else:
        return getWebsiteAssets(URLS_TO_CRAWL.pop(0))


def fetch(url):
    scraped_urls = []
    scraped_img_src = []
    try:
        if is_url_valid(url)
            page = urlopen(url)
            content = page.read()
            soup = BeautifulSoup(content, 'lxml', parse_only=SoupStrainer('a'))
            for anchor in soup.find_all('a'):
                link = anchor.get('href')
                if is_url_valid(link)
                    scraped_urls.append(link)

            for anchor in soup.find_all('img'):
                link = anchor.get('src')
                if is_url_valid(link):
                    scraped_img_src.append(link)

            scraped_urls = list(set(scraped_urls))  # To remove repitions
            scraped_img_src = list(set(scraped_img_src))  # To remove repitions
            URLS_TO_CRAWL.extend(scraped_urls)
            PARENT_LINK[url] = [scraped_urls, scraped_img_src]

    except HTTPError as e:
        print('HTTPError:' + str(e.code) + ' in ', url)
    except URLError as e:
        print('URLError: ' + str(e.reason) + ' in ', url)
    except Exception:
        import traceback
        print('Generic exception: ' + traceback.format_exc() + ' in ', url)

    return scraped_urls, scraped_img_src


if __name__ == '__main__':
    print('URL: ', args.url)
    getWebsiteAssets(args.url)
