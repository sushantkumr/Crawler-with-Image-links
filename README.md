#  Crawler-with-Image-links
Web Crawler written in Python using BeautifulSoup. Retrieves the hyperlinks and image links present in a webpage.

## Solution
The methods `fetch` and `get_website_assets` are a part of the class `Crawler` which are responsible for fetching links and image sources from a website depending on the depth specified.

## Steps to set it up
* If you wish to create a virtualenv, run the following command `virtualenv -p python3.7 .venv_links_fetcher` and activate the same by running `source .venv_links_fetcher/bin/activate`
* Install requirements by running `pip3 install -r requirements.txt` from the root of the repository
* Run the program using `python3 main.py` (Runs with default values of url as `https://mix.com` and depth as `1`)
* If you wish to specify your own values run it `-u` and `-d` arguments followed by respective values (Example: `python3 main.py -u www.google.com -d 10`)
* Run the tests using `python3 -m unittest discover`
