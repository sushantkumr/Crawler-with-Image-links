import argparse
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

parser = argparse.ArgumentParser(description='Simple Web Crawler')
parser.add_argument('-u', '--url', metavar='', default='https://mix.com',
                    type=str, help='Seed URL for crawling')
args = parser.parse_args()


def fetch(url):
    scraped_urls = []
    scraped_img_src = []
    try:
        page = urlopen(url)
        content = page.read()
        soup = BeautifulSoup(content, 'lxml', parse_only=SoupStrainer('a'))
        for anchor in soup.find_all('a'):
            link = anchor.get('href')
            scraped_urls.append(link)

        for anchor in soup.find_all('img'):
            link = anchor.get('src')
            scraped_img_src.append(link)

        scraped_urls = list(set(scraped_urls))  # To remove repitions
        scraped_img_src = list(set(scraped_img_src))  # To remove repitions

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
    links, image_sources = fetch(args.url)
    print(links)
    print(image_sources)
