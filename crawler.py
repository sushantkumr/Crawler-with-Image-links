from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from helpers import is_url_valid, get_clean_url


class Crawler():

    def __init__(self, url, depth=1):
        self.parent_link = {}
        if (is_url_valid(url)):
            url = get_clean_url(url, '')
            self.depth = depth
            self.urls_to_crawl = []
            self.get_website_assets(url)
        else:
            print('Invalid URL entered')


    def print_output(self):
        '''
        Print the lists of the URLs and Image sources collected
        @input:
            url: URL to be scraped
        '''
        for key, value in self.parent_link.items():
            print('\n\n')
            print('**********************************************************************************')
            print('PARENT LINK : ', key)
            print('\n')
            print(*value[0], sep='\n')
            print('HYPERLINKS: ', len(value[0]))
            print('\n')
            print(*value[1], sep='\n')
            print('IMAGE SOURCES: ', len(value[1]))
            print('**********************************************************************************')


    def get_website_assets(self, url):
        '''
        Calls fetch() depending on the depth required
        @input:
            url: URL to be scraped
        '''
        self.fetch(url)
        if (len(self.parent_link.keys()) == self.depth):
            return
        else:
            if len(self.urls_to_crawl) > 0:
                return self.get_website_assets(self.urls_to_crawl.pop(0))
            else:
                return


    def fetch(self, url):
        '''
        Crawl over URLs
            - scrape for anchor tags with hrefs in a webpage
            - reject if unwanted or cleanup the obtained links
            - append to a set to remove duplicates
            - "urls_to_crawl" is the repository for crawled URLs
        @input:
            url: URL to be scraped
        '''

        scraped_urls = []
        scraped_img_src = []
        try:
            if is_url_valid(url):
                page = urlopen(url)
                content = page.read()
                soup = BeautifulSoup(content, 'lxml')
                for anchor in soup.find_all('a'):
                    link = anchor.get('href')
                    if is_url_valid(link):
                        link = get_clean_url(url, link)
                        scraped_urls.append(link)
                    else:
                        pass

                for anchor in soup.find_all('img'):
                    link = anchor.get('src')
                    if is_url_valid(link):
                        link = get_clean_url(url, link)
                        scraped_img_src.append(link)
                    else:
                        pass

                scraped_urls = list(set(scraped_urls))  # To remove repitions
                scraped_img_src = list(set(scraped_img_src))  # To remove repitions

                self.urls_to_crawl.extend(scraped_urls)
                self.parent_link[url] = [scraped_urls, scraped_img_src]

        except HTTPError as e:
            print('HTTPError:' + str(e.code) + ' in ', url)
        except URLError as e:
            print('URLError: ' + str(e.reason) + ' in ', url)
        except Exception:
            import traceback
            print('Generic exception: ' + traceback.format_exc() + ' in ', url)
