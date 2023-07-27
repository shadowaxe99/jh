```python
class TestingInterface:
    def __init__(self):
        self.test_outputs = {}

    def run_tests(self, test_cases):
        results = {}
        for test_case in test_cases:
            try:
                result = test_case.run()
                results[test_case.name] = result
            except Exception as e:
                results[test_case.name] = str(e)
        return results

    def update_test_outputs(self, test_case_name, output):
        self.test_outputs[test_case_name] = output

    def retrieve_test_outputs(self, test_case_name):
        return self.test_outputs.get(test_case_name, "Test case not found")
```