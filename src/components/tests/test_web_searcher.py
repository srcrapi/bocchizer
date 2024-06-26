import unittest
import sys
import os

components_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(components_dir)

from web_searcher import WebSearcher


class TestWebSearcher(unittest.TestCase):
    def setUp(self):
        self.ws = WebSearcher()
        
    
    def test_search(self):
        search_term = "Dell 725y7"
        num_images = 5

        url_images = self.ws.search(search_term, num_images)
        
        self.assertEqual(len(url_images), num_images, f"Expected {num_images} images, but got {len(url_images)}")
        
        for url in url_images:
            if url.startswith("http"):
                self.assertTrue(url.startswith("http"), f"Invalid URL format: {url}")
            elif url.startswith("data:image"):
                self.assertTrue(url.startswith("data:image"), f"Invalid data URL format: {url}")
            else:
                self.fail(f"Invalid URL format: {url}")
                

if __name__ == "__main__":
    unittest.main()