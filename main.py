import argparse


parser = argparse.ArgumentParser(description='Simple Web Crawler')
parser.add_argument('-u', '--url', metavar='', default='https://mix.com',
                    type=str, help='Seed URL for crawling')
args = parser.parse_args()


if __name__ == '__main__':
    print('URL: ', args.url)

