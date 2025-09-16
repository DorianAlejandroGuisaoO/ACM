## Fase 6: Testing

### 6.1 Test básico (tests/test_bot.py)
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.bot import InstagramBot
from src.instagram_api import InstagramAPI

class TestInstagramBot(unittest.TestCase):
    def setUp(self):
        self.bot = InstagramBot()
        self.api = InstagramAPI()
    
    def test_hello_world(self):
        result = self.bot.hello_world()
        self.assertIn("Hello World", result)
    
    def test_api_connection(self):
        result = self.api.connect("test", "test")
        self.assertTrue(result)
    
    def test_response_generation(self):
        response = self.bot.simulate_post_response("Test post")
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main() 
