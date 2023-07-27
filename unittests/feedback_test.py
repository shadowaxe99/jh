```python
import unittest
from feedback import Feedback

class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.feedback = Feedback()

    def test_provide_feedback(self):
        self.feedback.provide_feedback("Test feedback")
        self.assertEqual(self.feedback.feedback_list[-1], "Test feedback")

    def test_tag_feedback(self):
        self.feedback.provide_feedback("Test feedback")
        self.feedback.tag_feedback(0, "Test")
        self.assertEqual(self.feedback.feedback_tags[0], "Test")

    def test_search_feedback(self):
        self.feedback.provide_feedback("Test feedback")
        self.feedback.provide_feedback("Another feedback")
        self.feedback.tag_feedback(0, "Test")
        self.feedback.tag_feedback(1, "Another")
        results = self.feedback.search_feedback("Test")
        self.assertEqual(results, ["Test feedback"])

if __name__ == '__main__':
    unittest.main()
```