import unittest
from unittest.mock import patch
from crawler import Crawler


class TestIsUrlInvalid(unittest.TestCase):

    def test_crawler_depth(self):
        url = 'https://mix.com/'
        depth = 1
        obj = Crawler(url, depth)
        self.assertEqual(1, len(obj.parent_link.keys()))

    def test_crawler_valid_urls_image_sources(self):
        valid_urls = """
            <a class="navigation-someclass" href="https://www.DUMMY_URL1.com">Word1</a>
            <a class="navigation-someclass" href="https://www.DUMMY_URL2.com">Word2</a>
            <a class="navigation-someclass" href="https://www.DUMMY_URL3.com">Word3</a>
            <a class="navigation-someclass" href="https://www.DUMMY_URL4.com">Word4</a>
            <a class="navigation-someclass" href="https://www.DUMMY_URL5.com">Word5</a>
            <img src="https://www.DUMMY_URL1.com/article_2_64k-082c964ab4006e04074fc7d94.jpg"></img>
            <img src="https://www.DUMMY_URL2.com/article_2_64k-082c964ab4a0064295c074fc7d94.jpg"></img>
            <img src="https://www.DUMMY_URL3.com/slides/article_2_64k-082c29fc7d94.jpg"></img>
            """

        valid_urls = str.encode(valid_urls)
        with patch("http.client.HTTPResponse.read") as mocked_urls:
            mocked_urls.return_value = valid_urls
            url = 'https://mix.com'
            depth = 1
            obj = Crawler(url, depth)
            self.assertEqual(1, len(obj.parent_link.keys()))
            self.assertEqual(5, len(obj.parent_link[url][0]))
            self.assertEqual(3, len(obj.parent_link[url][1]))

    def test_crawler_empty_link(self):
        url = ''
        depth = 15
        obj = Crawler(url, depth)
        self.assertEqual(0, len(obj.parent_link.keys()))
