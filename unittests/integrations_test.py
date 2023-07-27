```python
import unittest
from integrations import Integrations

class TestIntegrations(unittest.TestCase):

    def setUp(self):
        self.integrations = Integrations()

    def test_manage_integrations(self):
        result = self.integrations.manage_integrations('IDE1')
        self.assertEqual(result, 'Managed integration with IDE1')

    def test_update_integration_status(self):
        result = self.integrations.update_integration_status('IDE1', 'active')
        self.assertEqual(result, 'Updated integration status of IDE1 to active')

if __name__ == '__main__':
    unittest.main()
```