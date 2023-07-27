```python
import unittest
from visual_cues import VisualCues

class TestVisualCues(unittest.TestCase):

    def setUp(self):
        self.visual_cues = VisualCues()

    def test_update_agent_activity(self):
        result = self.visual_cues.update_agent_activity('active')
        self.assertEqual(result, 'Agent activity updated to active')

    def test_update_project_status(self):
        result = self.visual_cues.update_project_status('completed')
        self.assertEqual(result, 'Project status updated to completed')

    def test_update_code_output(self):
        result = self.visual_cues.update_code_output('No errors found')
        self.assertEqual(result, 'Code output updated to No errors found')

if __name__ == '__main__':
    unittest.main()
```