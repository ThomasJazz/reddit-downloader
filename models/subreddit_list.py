import json
class SubredditList():
    def __init__(self):
        self.subreddits = []
        self.name = None

    def get_json(self):
        json_dict = {'subreddits': [], 'name': self.name}

        for sub in self.subreddits:
            json_dict['subreddits'].append(sub.get_json())
        
        return json.dumps(json_dict)
    
    def from_json