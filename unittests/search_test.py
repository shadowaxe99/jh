```python
import unittest
from search import Search

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search = Search()

    def test_search_feedback(self):
        feedbacks = [
            {"id": 1, "feedback": "Great product!"},
            {"id": 2, "feedback": "Could be better."},
            {"id": 3, "feedback": "Loved the user interface!"},
        ]
        self.search.feedbacks = feedbacks

        result = self.search.search_feedback("Great")
        self.assertEqual(result, [feedbacks[0]])

        result = self.search.search_feedback("user interface")
        self.assertEqual(result, [feedbacks[2]])

        result = self.search.search_feedback("Not found")
        self.assertEqual(result, [])

    def tearDown(self):
        self.search = None

if __name__ == '__main__':
    unittest.main()
```