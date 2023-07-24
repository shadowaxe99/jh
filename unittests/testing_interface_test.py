```python
import unittest
from testing_interface import TestingInterface

class TestTestingInterface(unittest.TestCase):

    def setUp(self):
        self.testing_interface = TestingInterface()

    def test_run_tests(self):
        result = self.testing_interface.run_tests()
        self.assertIsNotNone(result)

    def test_update_test_outputs(self):
        test_output = "Test output"
        self.testing_interface.update_test_outputs(test_output)
        self.assertEqual(self.testing_interface.test_output, test_output)

    def test_retrieve_test_outputs(self):
        test_output = "Test output"
        self.testing_interface.update_test_outputs(test_output)
        result = self.testing_interface.retrieve_test_outputs()
        self.assertEqual(result, test_output)

if __name__ == '__main__':
    unittest.main()
```