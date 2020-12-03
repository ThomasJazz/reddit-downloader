class SubredditLists():
    def __init__(self):
        self.lists = {}
    
    def get_dict(self):
        return self.lists
    
    def add_subreddit(self, list_name: str, sub):
        if (list_name in self.lists):
            self.lists[list_name].append(sub)
        else:
            raise Exception(f'Error, subreddit list {list_name} does not exist')
    
    def create_list(self, list_name):
        self.lists[list_name] = []
