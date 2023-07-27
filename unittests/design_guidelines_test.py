```python
import unittest
from design_guidelines import DesignGuidelines

class TestDesignGuidelines(unittest.TestCase):

    def setUp(self):
        self.design_guidelines = DesignGuidelines()

    def test_check_simplicity(self):
        result = self.design_guidelines.check_simplicity()
        self.assertIsInstance(result, bool)

    def test_check_intuitiveness(self):
        result = self.design_guidelines.check_intuitiveness()
        self.assertIsInstance(result, bool)

    def test_check_responsiveness(self):
        result = self.design_guidelines.check_responsiveness()
        self.assertIsInstance(result, bool)

    def test_check_navigation(self):
        result = self.design_guidelines.check_navigation()
        self.assertIsInstance(result, bool)

    def test_check_unified_interface(self):
        result = self.design_guidelines.check_unified_interface()
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()
```