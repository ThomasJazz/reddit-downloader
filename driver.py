import os
import sys

from library import method_helper
from models import subreddit
from models import subreddit_list
from models import subreddit_lists

# Helper objects
helper = method_helper.MethodHelper()

# File paths
script_root = os.path.dirname(sys.argv[0])
config_path = helper.join_path(script_root, 'config/config.json')

# Data containers
config = None
sub_lists = None

if (helper.file_exists(config_path)):
    sub_lists = helper.load_pickle(config_path)
else:
    sub_lists = subreddit_lists.SubredditLists()

# Displays the main menu and returns the user input
def main():
    menu = '''
    [1] Download images from a subreddit
    [2] Add a new subreddit
    [3] Configure an existing subreddit
    [4] Create a new subreddit list
    [5] Save
    [0] Exit
    '''
    user_input = input(menu)
    return user_input

# [2] Add a new subreddit
def add_subreddit():
    sort_menu = '''
    [1] hot
    [2] top
    [3] new
    '''
    
    time_menu = '''
    [1] hour
    [2] day
    [3] week
    [4] month
    [5] year
    [6] all
    '''
    
    sub_name = input('Subreddit: ')
    dl_dir = input('Download directory: ')
    dl_limit = input('Download limit (0 for all): ')
    sort = input(sort_menu)
    time_frame = input(time_menu)
    sub_list = input('Add to subreddit list: ')

    sub = subreddit.Subreddit(sub_name, dl_dir, dl_limit, sort, time_frame)
    sub_lists.add_subreddit(sub_list, sub)

# [4] Create a new subreddit list
def create_subreddit_list():
    list_name = input('List name: ')
    sub_lists.create_list(list_name)

# [5]
def save_all():
    pass

# Main routine that loops the main() menu function
user_input = '1'
while (user_input != '0'):
    user_input = main()

    if (user_input == '2'):
        add_subreddit()
    elif (user_input == '3'):
        pass
    elif (user_input == '4'):
        create_subreddit_list()
    
    print()

helper.save_pickle(config_path, sub_lists)