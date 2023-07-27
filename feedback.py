```python
class Feedback:
    def __init__(self):
        self.feedback_list = []

    def provide_feedback(self, feedback):
        self.feedback_list.append(feedback)
        return "Feedback provided successfully."

    def tag_feedback(self, feedback, tag):
        for item in self.feedback_list:
            if item == feedback:
                item['tag'] = tag
        return "Feedback tagged successfully."

    def search_feedback(self, keyword):
        result = [item for item in self.feedback_list if keyword in item['feedback']]
        return result
```