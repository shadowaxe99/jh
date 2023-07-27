```python
class Integrations:
    def __init__(self):
        self.ide_integrations = {}

    def manage_integrations(self, ide_name, integration_details):
        self.ide_integrations[ide_name] = integration_details

    def update_integration_status(self, ide_name, status):
        if ide_name in self.ide_integrations:
            self.ide_integrations[ide_name]['status'] = status
        else:
            print(f"No integration found for {ide_name}")
```
