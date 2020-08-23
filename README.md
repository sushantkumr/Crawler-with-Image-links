#  Crawler-with-Image-links
Web Crawler written in Python using BeautifulSoup. Retrieves the hyperlinks and image links present in a webpage.

## Steps to set it up
* Install requirements by running `pip3 install -r requirements.txt`
* Run the program using `python3 main.py` (Runs with default values of url as `https://mix.com` and depth as `1`)
* If you wish to specify your own values run it `-u` and `-d` arguments followed by respective values (Example: `python3 main.py -u www.google.com -d 10`)
* Run the tests using `python3 -m unittest discover`
