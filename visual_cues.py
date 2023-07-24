```python
class VisualCues:
    def __init__(self):
        self.agent_activity = {}
        self.project_status = {}
        self.code_output = {}

    def update_agent_activity(self, agent_id, activity):
        self.agent_activity[agent_id] = activity

    def update_project_status(self, project_id, status):
        self.project_status[project_id] = status

    def update_code_output(self, code_id, output):
        self.code_output[code_id] = output
```