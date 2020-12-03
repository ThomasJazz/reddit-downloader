"""
Last Update: 1/16/20
Creation Date: 7/25/19
########################################################
# Summary
########################################################
Methods to assist in standard Python script development

########################################################
# Class Requirements
########################################################
Requirements: None

########################################################
# Functions
########################################################

########################
# Utility Functions
########################
---------------------------------------------------------------------
cut_paste_file(source: str, destination: str, override=False)
-Summary: Cuts and paste files from source to destination
-Args:
    1) source - full path of the file including the file name
        Example: source = "C:/Users/shuynh/Desktop/testFile.txt" 
    2) destination - full path of the file including the file name
-Optional Args:
    3) (bool) override=False - boolean value for whether or not to override existing files
-Returns: None
---------------------------------------------------------------------
copy_paste_file(source: str, destination: str, override=False)
-Summary: Copies and pastes file from source to destination
-Args:
    1) source - full path of file to be copied, including file name
        Example: source = "C:/Users/shuynh/Desktop/testFile.txt"
    2) destination - full path of the file including the file name
-Optional Args:
    3) (bool) override=False - boolean value for whether or not to override existing files
-Returns: None
---------------------------------------------------------------------
file_exists(filepath: str)
-Summary: Checks if a file exists and makes sure that it is not empty
-Args:
    1) file_path - full path of the file including the file name
        Example: file_path = C:/Users/shuynh/Desktop/testFile.txt"
-Returns: True/False
---------------------------------------------------------------------
get_file_name(file_path: str)
-Summary: Gets the file name from the full path
-Args:
    1) file_path - full path of the file who's name you wish to find
        Example: file_path = "C:/Users/shuynh/Desktop/testFile.txt"
-Returns: name of file
    Example: "testFile.txt"
---------------------------------------------------------------------
archive_files(src: str, dest='', extension='')
-Summary: Moves all files in src directory to _Archive folder
-Args:
    1) src - directory of files to be archived (needs '/' at end of string)
        Example: src = "C:/Users/shuynh/Desktop/"
-Optional Args:
    2) (str) dest=src + "_Archive/"
        Example: dest = "C:/Users/shuynh/Documents/"
    3) (str) extension= '' - Archive only files with given extension
        Example: extension = '.xlsx'
-Returns: None
---------------------------------------------------------------------
copy_files_to_dir(src: str, dest: str, extension='', contains='', include_dirs=False)
-Summary: Copies all files in 'src' directory to 'dest' directory
-Args:
    1) src - directory of files to be copied
        Example: "C:/Users/shuynh/Desktop/"
    2) dest - directory to be copied to
        Example: "C:/Users/shuynh/Documents/"
-Optional Args:
    3) (str) extension='' - Copy only files with given extension
        Example: extension = '.xlsx'
    4) (str) contains='' - Copy only files that contain value in 'contains'
        Example: contains = 'SEP'
    5) (bool) include_dirs=False - Dictates whether or not directories are copied as well
        Example: include_dirs = True
---------------------------------------------------------------------
get_files_in_dir(dir: str)
-Summary: Returns a list of all the files in a given directory, excluding directories
-Args:
    1) dir - Directory to list contents of
        Example: "C:/Users/shuynh/Documents/"
-Returns: ["list.txt", "of.mp3", "files.txt"]
---------------------------------------------------------------------
copy_paste_file_structure(self, src_dir: str, dest_dir: str)
-Summary: Copies the underlying folder structure to another folder. Will create the destination
    folder if it does not exist
-Args
    1) src_dir - directory of the folder structure to be copied
        Example: "C:/Users/shuynh/Documents/"
    2) dest_dir: directory to be copied to
---------------------------------------------------------------------
check_and_create_directory(self, folder_path: str, add_archive=None):
-Summary - Checks if a folder/address path exists and creates it if it doesn't. It has an optional
    parameter that will add a _Archive folder in the new directory
-Args
    1) folder_path - The directory or folder to be created:
        Example: "C:/Users/shuynh/Documents/new_folder/"
-Optional Args
    2) (boolean) add_archive - Will add an _Archive folder to the newly created folder
        Example: "C:/Users/shuynh/Documents/new_folder/" --> "C:/Users/shuynh/Documents/new_folder/_Archive/"




---------------------------------------------------------------------
########################
# Conversion Functions 
########################
---------------------------------------------------------------------
convert_obj_to_lst(lst_of_objects: lst, include_header=True)
-Summary: Converts a list of objects into a 2d list. Will return headers using the attribute names
    if it is specified.
-Args:
    1) lst_of_objects - list of objects
        Example: [workorder_obj1, workorder_obj2, workorder_obj3]
-Optional Args:
    2) (bool) include_header=True - Determines if the variable names are returned as headers
        Example: False
-Returns:   [['workorder', 'obj1', 'as', 'list'], ['workorder', 'obj2', 'as', 'list'], 
            ['workorder', 'obj3', 'as', 'list']]
        or (with include_header = False)
            [['header_col1', 'header_col2', 'header_col3', 'header_col4'], ['workorder', 'obj1', 'as', 'list'],
            ['workorder', 'obj2', 'as', 'list'], ['workorder', 'obj3', 'as', 'list']]
---------------------------------------------------------------------
convert_obj_attributes_to_lst(class_obj, return_header=False)
-Summary: Transforms objects attributes to key-value pairs in dict then return in form of list.
    This function will skip over any data types that are containers(lists, dictionaries, objects..etc)
-Args:
    1) class_obj - Class object of any type
-Optional Args:
    2) return_header - returns a list with the name of the object attributes rather than the attribute values
-Returns
    ['workorder', 'obj2', 'as', 'list']
or (with include_header = True)
    ['header_col1', 'header_col2', 'header_col3', 'header_col4']
---------------------------------------------------------------------
convert_lst_of_dict_to_2dlst(self, lst_of_dict: List[Dict], return_header=False):
-Summary - Converts a list of dictionaries to a 2d list. If return_header is True, it will
    return a header in as the first list using the dictionary keys as the header names
-Args:
    1) lst_of_dict - a list of dictionaries
        Example: [{'key1': 'value1', 'key2': 1}, {'key1': 'value2', 'key2': 2}]
-Optional Args:
    2) (boolean) return_header - If True, it will return the headers (example below)
-Returns
    [['value1', 1], ['value2', 2]]
or with return_header=True
    [['key1',key2'], ['value1', 1], ['value2', 2]]

---------------------------------------------------------------------
convert_2dlist_to_lst_of_dict(self, lst_of_lst)
-Summary: Converts 2d list into list of dictionaries
-Args:
    1) data_lst - 2d list of data - data lst MUST have a header
    [['header1','header2'], ['data1','data2'], ['data3','data4']]

-Returns: [{'header1':'data1', 'header2': 'data2'},{'header1':'data3', 'header2': 'data4'}]
---------------------------------------------------------------------
set_class_obj(class_obj: obj, data_dct: dict)
-Summary: Takes key, value pairs from dictionary and assigns them to object variables
-Args:
    1) class_obj - empty object to assign data to
    2) data_dct - dictionary to pull data from
-Returns: object_of_type_class_obj
---------------------------------------------------------------------
clean_lst_for_bulk_insert(self, data_lst: List)
-Summary- Takes a 2d list a removes all strings and fixes datetimes that would cause issues
    for a SQL server bulk insert
-Arg
    1) A 2d List
-Return
    Returns a list with no commas, double quotes, and etc...
----------------------------------------------------------------------


########################
# Time Functions
########################
---------------------------------------------------------------------
get_current_date()
-Summary: date in string format (ie. 20190801 for 8/1/19)
-Returns: 20190801
---------------------------------------------------------------------
get_current_datetime()
-Summary: datetime in string format (ie. 20190801-152101 for 8/19/19 3:21 PM)
-Returns: 20190801-152101
---------------------------------------------------------------------
########################
# Time Functions
########################
---------------------------------------------------------------------
get_current_date()
-Summary: date in string format (ie. 20190801 for 8/1/19)
-Returns: 20190801
---------------------------------------------------------------------
get_current_datetime()
-Summary: datetime in string format (ie. 20190801-152101 for 8/19/19 3:21 PM)
-Returns: 20190801-152101
---------------------------------------------------------------------
########################
# Email and Logging Functions 
########################
add_log(path: str, message: str, automation_status: str, level: str, script_type: str, msg_dct={}, ignore_splunk_timer=False):
-Summary - Creates a log, or appends to it, or adds the last line. There is a lot going on here
    so READ this if you need help.
-Args
    1) path - sets the path where your log file will be created or appended to
        - Example: C:\Data\splunk\example_log20200110.txt
    2) message - sets a custom message for your log at that particular line
        - Example: "Part 1:Pulling Data"
    3) automation_status - sets the status of the log. You MUST choose "BEGIN", "END", "IN-PROGRESS"
        - BEGIN will create the log file
        - if automation_status="END" and level="ERROR", sys.exit() will be called and close the script out
    4) level - sets the error level. You MUST choose "INFO", "WARNING", "ERROR", "CRITICAL"
        - if automation_status="END" and level="ERROR", sys.exit() will be called and close the script out
    5) script_type - sets what kind of script the log is tracking. You must choose
        'REPORT', 'DATA', 'UTILITY', or 'PROCESS'
- Optional Args:
    6) (dictionary) msg_dct - if you add a dictionary, it will append to the message:
        - Example: timestamp="2020-01-09 18:46:43.746959Z" | level="INFO" | type="REPORT" | automation_status="IN-PROGRESS" | script_name="billing_report_cbre_ups_all_workorder_data_no_pivot.py" | ignore_splunk_timer="False" | message="Connecting to DB and Executing Query" 
            If msg_dct={"category":"test", "loc":"AZ"}, you would get:
            timestamp="2020-01-09 18:46:43.746959Z" | level="INFO" | type="REPORT" | automation_status="IN-PROGRESS" | script_name="billing_report_cbre_ups_all_workorder_data_no_pivot.py" | ignore_splunk_timer="False" | message="Connecting to DB and Executing Query" | category="test" | loc="AZ"
    7) (boolean) ignore_splunk_timer - This does nothing in the actual function itself. This was made for
        Splunk where all our logs go. Timed alerts will be ignored if this is set to True.
        You generally don't have to worry about this at all if you aren't dealing with script alerts.

--------------------------------------------------------------------
add_message(message: str, newlines: int)
-Summary: Appends the $message string in the class for email and logging purposes. Can add a <br />
    into the message string to indicate break. When using 'WriteLog' function to write to log, the
    break will be replaced with a newline for logging(n).
-Args:
    1) (string) message - text for logging and email
        Example: $message = "An error has occurred..."
    2) (int) newlines - adds x number of newlines after the message
-Values Returned: None
---------------------------------------------------------------------
get_message()
-Summary: Converts the message from HTML break format to Python newline format and returns the message to the user 
-Args: None
-Values Returned: $message
---------------------------------------------------------------------
clear_message()
-Summary: Clears the message string
-Args: None
-Values Returned: None
---------------------------------------------------------------------
send_email(self, email_to, subject: str, message = None, email_cc = None, attachment = None, reply_to = None)
-Summary: Sends an email with optional message, cc, and attachments
-Args:
    1) email_to (can be sent as a list or string of email addresses)
    2) subject 
    3) (opt) message - Body message of the email - you can send html through here
    4) (opt) attachment - Attachment of the file
    5) (opt) reply_to - Send an email address to reply to (can be one or multiple separated by ';')

-Error Returned:
    1) Error has occurred


########################
# Read & Write Functions
########################
read_excel(self, file_path: str, sheet_name=None, formatting="list")
-Summary: Reads and excel file and returns a <List<List>> or <List<Dictionary>>. Will read
    the first sheet in the excel file unless specified otherwise
-Args:
    1) file_path = path string of the location of excel file
        Example: "C:/Users/kbui/Documents/Github Repositories/fs-automation-python/file_name.xlsx"
-Optional Args:
    2) (string) sheet_name - Targets a specific sheet/tab name in the excel file. Use this if there are 
        Multiple sheets you need to read or only a specific one.
    3) (string) formatting - Tells the function what format to return. Use 'list' or 'dictionary'
        By Default, it will return <List<List>>. If 'dictionary' is used, the function will return <List<Dictionary>>
-Return: <List<List>> or <List<Dictionary>>

---------------------------------------------------------------------
write_to_excel_sheets(file_path: str, data_dict: Dict[str, List[List]])
-Summary: Writes a dictionary of <List<List>> to an excel file. Can output data to multiple sheets
-Args:
    1) file_path - please provide a string path for where you want the file to go
        Example: "C:/Users/kbui/Documents/Github Repositories/fs-automation-python/file_name.xlsx"
    2) data_dict - make sure the keys are the Names for the sheet(s) you want to output data to. 
        Example: {'sheet_name1':[['header1', 'header2'], ['data1', 'data2']],
                   'sheet_name2':[['header1', 'header2', header3], ['data1', 'data2', 'data3']]     }
        - The example will create sheet_name1 and sheet_name2 will their respective datasets/values

---------------------------------------------------------------------
write_to_excel(file_path: str, data_lst: list, sheet_name="Report")
-Summary: Creates xlsx file at file_path and write data from a List[List]
-Args: 
    1) file_path - please provide a string path for where you want the file to go
        Example: "C:/Users/kbui/Documents/Github Repositories/fs-automation-python/file_name.xlsx"
    2) data_lst - a 2d lst containing data
        Example: [['header1', 'header2', header3], ['data1', 'data2', 'data3']]
-Optional Args:
    3) (string) sheet_name - will name the sheet of the excel file being written to. By default, it is
        named "Report".
---------------------------------------------------------------------
read_csv(self, file_path: str, delimiter=",")
-Summary: Reads a csv file and returns a list of lists
-Args:
    1) file_path - full path of file to read
-Optional Args:
    2) (string) - delimiter - choose the string to use to separate the data
-Returns: List[List]
---------------------------------------------------------------------
write_to_csv(self, file_path: str, data_lst: List[List], _delimiter=',', _quoteall=False)
-Summary: Creates new csv file at file_path and populates with data from dataset
-Args:
    1) file_path - full path of output file
        Example: "C:/Users/kbui/Documents/Github Repositories/fs-automation-python/file_name.csv"
    2) data_lst - 2d list to be written to csv file
        Example: [['header1', 'header2', header3], ['data1', 'data2', 'data3']]
-Optional Args:
    3) (string) - delimiter - choose the string to use to separate the data
    4) (boo'ean) _quoteall - Set to True if you want every item to be surrounded by double quotes.
        Beware, not all csv readers can pikc this up.
-Returns: None
---------------------------------------------------------------------
append_to_csv(self, file_path, data_lst: List[List], _delimiter=',', _quoteall=False)
-Summary: Appends a row of data to an existing csv file
-Args:
    1) file_path - name of file to which data will be appended
        Example: "C:/Users/kbui/Documents/Github Repositories/fs-automation-python/file_name.csv"
    2) data_lst - data lst to be appended to the csv file
        Example: ['data1', 'data2', 'data3']
-Optional Args:
    3) (string) - delimiter - choose the string to use to separate the data
    4) (boo'ean) _quoteall - Set to True if you want every item to be surrounded by double quotes.
        Beware, not all csv readers can pikc this up.
-Returns: None
---------------------------------------------------------------------


########################
# Usage Example
########################
from library import method_helper   #Used to assist with running methods

# Sets up the helper object
helper = method_helper.MethodHelper()

# Sets up the email address information for the automation team
email_to = ["Solomon.Huynh@cbre.com", "Kevin.Bui@cbre.com"]
email_subject = "Script Notification - sample_script.py"
helper.add_message("Script Name: sample_script.py", 1)


########################
# Change Log
########################
8/19/19 - Added Documentation to the class

#>

"""

from typing import Dict   # Typing library used to give clarity for data types when making functions
from typing import List   # Ex - write_to_excel_sheets(self, file_path: str, data_dict: Dict[str, List[List]])


from datetime import *                          # Used for datetime functions
import time
from os.path import isfile, join                # Used for archiving
import ntpath                                   # Used to get file name on full URLs
import os                                       # Used for operating system commands
import sys                                      # Used for operating system commands
import smtplib                                  # Used to relay mail to the SMTP server
import shutil                                   # Used for cut_paste_file
import xlsxwriter                               # Used for export_list_to_xlsx
import subprocess                               # Used to call Windows commands 
import csv
import hashlib                                  # Used for insert_row_hashes_to_2dlist
import pickle
import pandas as pd
import math
import json

class MethodHelper:
    def __init__(self):
        # Used for script analytics
        self.start_time = datetime.utcnow()

    #############################
    # File Utility Methods
    #############################
    def delete_file(self, file_path: str):
        if not(self.file_exists(file_path)):
            raise f'Error, file {file_path} does not exist'

        os.remove(file_path)
    
    # Deletes all the files in the top level of a directory excluding those specified in excludes
    def delete_files_in_dir(self, folder: str, excludes=None):
        if not(os.path.isdir(folder)):
            raise f'Error, {folder} is not a valid directory'
        
        files = self.get_files_in_dir(folder, full_path=True)

        # Remove anything that contains a substring specified in excludes list
        if (excludes):
            filtered = []

            for file in files:
                if not(any(word in file for word in excludes)):
                    filtered.append(file)

            files = filtered

        for file in files:
            os.remove(file) 

    # Function that cuts and pastes the file from source to destination
    def cut_paste_file(self, src: str, dest: str, override=False):
        # Check that there is not a file at the destination
        if (self.file_exists(dest) and override == False):
            assert(False), 'Failed to cut/paste file. File already exists at destination: {0}'.format(dest)
        else:
            shutil.move(src, dest)
        
        if (self.file_exists(src)):
            assert(False), 'Failed to cut/paste file. File still exists at source: {0}'.format(src)
        
    
    # Function that copies and pastes the file from source to destination
    def copy_paste_file(self, src: str, dest: str, override=False):
        assert not(self.file_exists(dest) and override == False), ("File already exists at copy destination: {0}".format(dest))
        shutil.copy(src, dest)
        assert (self.file_exists(dest)), "Failed to copy file {0}".format(src)
        
        
    # Checks if a file exists
    @staticmethod
    def file_exists(file_path: str):
        try:
            if (os.path.exists(file_path) == False) or (os.stat(file_path).st_size == 0):
                return False
        except:
            return False
        return True


    # Gets the file name from the full path
    @staticmethod
    def get_file_name(file_path: str):
        return ntpath.basename(file_path)


    # Archive EVERY file in the 'src' directory
    def archive_files(self, src: str, dest='', extension='', contains='', override=False):
        if (dest == ''):
            dest = src + '_Archive/'

        assert (os.path.isdir(dest)), "[Error] Archive folder does not exist: {0}".format(dest)
        
        lst_files = self.get_files_in_dir(src)
    
        # Make sure there are actually files to archive
        if (len(lst_files) > 0):
            for file in lst_files:
                if (contains in file and file.endswith(extension)):
                    src_filename = src + file
                    dest_filename = dest + file
                    try:
                        if override is True:
                            self.cut_paste_file(src_filename, dest_filename, override=override)
                        else:
                            self.cut_paste_file(src_filename, dest_filename)
                        assert(self.file_exists(dest_filename) and not self.file_exists(src_filename)), "Warning, failed to archive file: {0}".format(dest_filename)
                    except Exception as e:
                        print(e)
                        return 0
        
        return 1
        

    # Copy EVERY file in the 'src' directory to the 'dest'
    def copy_files_to_dir(self, src: str, dest: str, extension='', contains='', include_dirs=False, override=False):
        lst_files = []
        if (include_dirs):
            lst_files = os.listdir(src)
        else:
            lst_files = [f for f in os.listdir(src) if isfile(join(src, f))]

        if (len(lst_files) > 0):
            for file in lst_files:
                if (file.endswith(extension) and contains in file):
                    src_filename = src + file
                    dest_filename = dest + file

                    self.copy_paste_file(src_filename, dest_filename, override=override)
        

    # Returns a list of all files in dir minus any sub directories
    def get_files_in_dir(self, src: str, contains='', include_dirs=False, full_path=False):
        lst_files = []
        
        if (include_dirs):
            lst_files = os.listdir(src)
        else:
            lst_files = [f for f in os.listdir(src) if isfile(join(src, f)) and contains in f]

        if (full_path):
            for i in range(0, len(lst_files)):
                lst_files[i] = os.path.join(src, lst_files[i])
        return lst_files


    # Recursively retrieve all files and subfiles with contains value in them
    # Because it's recursive, all files in returned list will include the full path, unlike get_files_in_dir
    def get_files_in_dir_recursive(self, src: str, contains=''):
        files = []
        for root, directories, filenames in os.walk(src):
            for filename in filenames:
                full_path = os.path.join(root, filename)
                if (contains in full_path):
                    files.append(full_path)
        
        return files


    # Recursively copies the underlying folder structure from src_dir to dest_dir.
    def copy_paste_file_structure(self, src_dir: str, dest_dir: str):
        if (os.path.isdir(src_dir)):
            if not(os.path.isdir(dest_dir)): # Create destination directory if it doesn't already exist
                os.mkdir(dest_dir)

            for r, d, f in os.walk(src_dir):
                if (os.path.isdir(r)):
                    sub_dir = r.replace(src_dir, '')
                    new_dir = dest_dir + sub_dir
                    try:
                        if not(os.path.isdir(new_dir)):
                            os.mkdir(new_dir)
                        if not(os.path.isdir(new_dir)):
                            raise FileNotFoundError
                    except Exception as e:
                        print(str(e))


    # Checks if a address path exists and creates it if it doesn't 
    def check_and_create_directory(self, folder_path: str, add_archive=None):
        # Adding _Archive Folder in new directory
        if add_archive is True:
            folder_path = os.path.join(folder_path, "_Archive/")

        if os.path.exists(folder_path):
            pass
        else:
            os.makedirs(folder_path)

    #############################
    # Conversion Methods
    #############################
    # Converts a list of objects into a 2d list
    def convert_obj_to_lst(self, lst_of_objects: List, include_header=True):
        data_lst = []  # Used to store the data inside the class objects

        # Error handling
        if not(isinstance(lst_of_objects, list)):
            raise Exception("Invalid Argument - Please pass a list of objects")
        elif len(lst_of_objects) == 0:
            raise Exception("The list passed to the function is empty")
        
         # Appends the row of headers from the object to the data_lst
        if include_header:
            header_lst = self.convert_obj_attributes_to_lst(lst_of_objects[0], return_header=True)
            data_lst.append(header_lst)

        # Appends the row of data from the object to the data_lst
        for row in lst_of_objects:

            temp_lst = self.convert_obj_attributes_to_lst(row, return_header=False)
            data_lst.append(temp_lst)
        return data_lst


    # Takes an object and strips out the attributes into a list
    def convert_obj_attributes_to_lst(self, class_obj, return_header=False):
        obj_dct = class_obj.__dict__   # transforms objects attributes to key-value pairs in dict
        return_lst = []
        for key in obj_dct:
            value_type = type(obj_dct[key])
            if value_type is list or value_type is dict:  # will skip attributes that are lists/dicts
                continue
            else:
                if return_header:
                    return_lst.append(key)
                else:
                    return_lst.append(obj_dct[key])

        return return_lst
    
    # Convert a lists of lists into a list of dictionaries
    def convert_2dlst_to_lst_of_dict(self, lst_of_lst: List[List]):
        return_lst = []
        headers_lst = lst_of_lst[0]
        for row in lst_of_lst:
            zipped_dict = dict(zip(headers_lst, row))
            return_lst.append(zipped_dict)

        return return_lst

    # Map a list of dicts to a dict where the key is the value of the column in key_map_string
    def map_lst_of_dicts_to_dict(self, key_map_string, list_dct):
        return_dct = {}
        for dct in list_dct:
            if dct[key_map_string] not in dct:
                return_dct[dct[key_map_string]] = dct
        return return_dct

    # Takes the key, value pairs in a dictionary and set an class object's attributes
    def set_class_obj(self, class_obj, data_dct: Dict):
        obj_dct = class_obj.__dict__
        for header_key in data_dct:
            # Only sets items if they exist in the class's attributes
            if header_key in obj_dct:
                setattr(class_obj, header_key, data_dct[header_key])
        return class_obj


    def strip_characters_from_lst(self, dataset: list, characters: list):
        for i in range(0, len(dataset)):
            for k in range(0, len(dataset[i])):
                if not(isinstance(dataset[i][k], str)):
                    continue
                for char in characters:
                    dataset[i][k] = dataset[i][k].replace(char, '')
    

    # Cleans a 2d list for csv files for sql bulk insert 
    def clean_lst_for_bulk_insert(self, data_lst: List, rowterminator='\r\n', fieldterminator=','):
        cleaned_data = []
        for i in range(0, len(data_lst)):
            row = data_lst[i]
            for k in range(0, len(row)):
                if (isinstance(row[k], str)):
                    current_string = row[k] # Strip field and row terminators
                    current_string = current_string.replace(rowterminator, '')
                    current_string = current_string.replace(fieldterminator, '')
                    current_string = current_string.replace('"', '')
                    current_string = current_string.replace('\r', '')
                    current_string = current_string.replace('\n', '')
                    row[k] = current_string

                    if (row[k].lower() == 'true'):
                        row[k] = 1
                    elif (row[k].lower() == 'false'):
                        row[k] = 0
                elif (isinstance(row[k], bool)):
                    if (row[k] is True):
                        row[k] = 1
                    elif (row[k] is False):
                        row[k] = 0

            cleaned_data.append(row)
        
        return cleaned_data
        

    # Converts all elements of a 2d list to be of type string so it can then be exported
    def convert_lst_items_to_str(self, data_lst):
        str_data_lst = []
        for i in range(0, len(data_lst)):
            items = data_lst[i]
            for k in range(0, len(items)):
                item = items[k]
                if isinstance(item, str):           # Don't change anything with strings
                    continue

                if item is None:                    # Set None to empty quotes
                    data_lst[i][k] = ''
                elif isinstance(item, datetime):    # Convert datetime to str
                    data_lst[i][k] = item.strftime('%Y-%m-%d %H:%M:%S.%f')
                else:                               # Cast all other types to str
                    data_lst[i][k] = str(item)

            str_data_lst.append(data_lst[i])

        return str_data_lst

    
    # for each row, starting at first_row, insert the md5 hash of that row in the specified column in the 2d list
    def insert_row_hashes_to_2dlist(self, dataset: list, column_name='row_hash', first_row=1, insert_col=0):
        # Set column header
        dataset[0].insert(insert_col, column_name)

        # Insert row hash values
        for i in range(first_row, len(dataset)):
            row = dataset[i]
            row_str = str(row)
            row_hash_obj = hashlib.md5(row_str.encode())
            row_hash = row_hash_obj.hexdigest()
            dataset[i].insert(insert_col, row_hash)


    def get_unique_rows_from_2dlist(self, dataset: list, master_hash: set, hash_col=0, first_row=1, include_header=False):
        unique_rows = []
        if (include_header):
            unique_rows = [dataset[0]]

        for row in dataset[first_row:]:
            if row[hash_col] not in master_hash:
                unique_rows.append(row)
        
        return unique_rows


    # Maps a list of dicts to a dict of dicts
    def map_list_of_dict_by_col(self, dataset: list, key_column: str, unique=False):
        mapped_dict = {}

        if (unique):
            for row in dataset:
                col_value = row[key_column]
                
                if (col_value not in mapped_dict):
                    mapped_dict[col_value] = row
                else:
                    raise f'Error. Key {col_value} already exists in dict'
        else:
            for row in dataset:
                col_value = row[key_column]
                
                if (col_value not in mapped_dict):
                    mapped_dict[col_value] = []
                
                mapped_dict[col_value].append(row)

        return mapped_dict

    # Converts a mapped dict of dicts to a 2d list
    # If unique is False, this implies that each key contains a list of data so we need to account for that
    def convert_mapped_dict_to_lst(self, dataset: dict, unique=False):
        output_lst = []

        # Add the headers
        for key in dataset:
            if (unique):
                output_lst.append(list(dataset[key].keys()))
            else:
                output_lst.append(list(dataset[key][0].keys()))
            break

        # Add the rest of the data
        if (unique):
            for key in dataset:
                output_lst.append(list(dataset[key].values()))
        else:
            for key in dataset:
                for record in dataset[key]:
                    output_lst.append(list(record.values()))
        
        return output_lst
                

    #############################
    # Time Methods
    #############################
    # returns date in string format with 4 digit year, 2 digit month and 2 digit day (ie. 20190801 for 8/1/19)
    def get_current_date(self, utc=False, formatting=None):
        time = None
        if (utc):
            time = datetime.utcnow()
        else:
            time = datetime.today()
        
        if (formatting is not None and formatting.lower() == 'sql'):
            return time.strftime('%Y-%m-%d')
        else:
            return time.strftime('%Y%m%d')

    # returns datetime in string format with 4 digit year, 2 digit day, "-", HHMMSS for time (ie. 20190801-152101 for 8/19/19 3:21 PM)
    def get_current_datetime(self, utc=False, formatting=None):
        time = None
        if (utc):
            time = datetime.utcnow()
        else:
            time = datetime.today()

        if (formatting is not None and formatting.lower() == 'sql'):
            return time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return time.strftime('%Y%m%d-%H%M%S')


    def get_current_time_obj(self, utc=False):
        if (utc):
            return datetime.utcnow()
        else:
            return datetime.today()

    # Get the time the script started
    def get_start_time(self):
        return self.start_time

    # Get the time elapsed since object initialization
    def get_elapsed_time(self):
        elapsed_time = datetime.utcnow() - self.start_time
        return elapsed_time
        #return round(elapsed_time, 6)
    
    def get_time_diff(self, start, end):
        return end - start

    # Builds a space-separated block of text
    # Accepts a string or a list of strings
    def surround_text(self, text, sep_multiplier=1.2, character='#'):
        if (isinstance(text, str)):
            text = [text]
        elif (not(isinstance(text, list))):
            text = str(text)
            text = [text]
        
        output_str = ''
        sep = character
        line_prefix = character*3
        sep_len = 9
        max_len = 9
        
        # Get max string length
        for i in range(0, len(text)):
            text[i] = str(text[i])  # Convert all list elements to string
            msg = text[i]

            if len(msg) > max_len:
                max_len = len(msg)
        
        # Determine length of sep based on max string length
        if (max_len * sep_multiplier > sep_len):
            sep_len = int(max_len * sep_multiplier) + 6 + (max_len % 2)
        
        sep = sep * sep_len
        # Begin the message block with the full separator
        output_str += sep + '\n'

        for msg in text:
            line = ''
            space = ' '
            insert_spaces = len(sep) - (len(msg) + (len(line_prefix) * 2))
            
            if insert_spaces % 2 == 0:
                space = space*(int(insert_spaces/2))
                line = line_prefix + space + msg + space + line_prefix
            else:
                space = space*(int(math.ceil(insert_spaces/2)))
                line = line_prefix + space + msg + space[1:] + line_prefix
            
            output_str += line + '\n'   # Append message to block

        # End the message block with the full separator
        output_str += sep
        
        return output_str
        

    #############################
    # Read & Write Methods
    #############################
    # Reads and excel file and returns a <List<List>> or <List<Dictionary>>
    def read_excel(self, file_path: str, sheet_name=None, formatting="list"):
        temp_lst = []

        # Error handling
        if not(isinstance(file_path, str)):
            raise Exception("Please enter a string into the file_path parameter")
        elif not(isinstance(formatting, str)):
            raise Exception("Please enter a string into the formatting parameter")
        elif sheet_name is not None:
            if (isinstance(sheet_name, str)):
                raise Exception("Please enter a string into the sheet_name parameter")
        elif formatting not in ["list", "dictionary"]:
            raise Exception("Please enter 'list' or 'dictionary' into the formatting parameter")

        # Reading excel file into a dataframe
        if sheet_name is not None:
            data_frame = pd.read_excel(file_path, sheet_name, encoding='utf-8')
        else:
            data_frame = pd.read_excel(file_path, encoding='utf-8')

        # Removing NaN values and replacing with None
        df = data_frame.where((pd.notnull(data_frame)), None)

        # Converting Dataframe to lists
        header_lst = df.columns.tolist()
        value_lst = df.values.tolist()

        # Concatenating data to <List<List>> or <List<Dictionary>>
        if formatting == 'list': # List Format
            temp_lst.append(header_lst)
            temp_lst += value_lst

        elif formatting == 'dictionary':  # Dictionary Format
            for row in value_lst:
                zipped_dict = dict(zip(header_lst, row))
                temp_lst.append(zipped_dict)

        return temp_lst


    # Writes dictionary of <string>:<List<List>> to an xlsx file. Can be used to write to multiple sheets.
    def write_to_excel_sheets(self, file_path: str, data_dict: Dict[str, List[List]]):
        try:
            # Starting workbook object at given file_path
            workbook = xlsxwriter.Workbook(file_path)
            datetime_format = workbook.add_format({"num_format": "yyyy/mm/dd hh:mm:ss"})  # adding a datetime format

            # Cycling through dictionary keys - keys will be used a sheet names
            for sheet_name_key in data_dict:
                data_set = data_dict[sheet_name_key]
                worksheet = workbook.add_worksheet(sheet_name_key) # Adding a new sheet per key

                # Cycling through 2d list inside data_dict
                for row_number, row in enumerate(data_set):
                    for col_number, item in enumerate(row):
                        # Outputting data to excel sheet
                        if (isinstance(item, datetime)):  # Writes datetime if applicable
                            worksheet.write_datetime(row_number, col_number, item, datetime_format)
                        else:
                            worksheet.write(row_number, col_number, item)

        except Exception:
            return 0
        finally:
            workbook.close() # closing workbook and creating file

    # Writes an excel file to 'file_path' with values in 2d list named 'data'
    def write_to_excel(self, file_path: str, data_lst: list, sheet_name="Report", date_fmt='%m/%d/%Y'): 
        book = xlsxwriter.Workbook(file_path)                       # Make new workbook
        sheet = book.add_worksheet(sheet_name)

        for row in range(0, len(data_lst)):
            for col in range(0, len(data_lst[row])):
                report_item = data_lst[row][col]
                
                if not(report_item is None):
                    if (isinstance(report_item, date) or isinstance(report_item, datetime)): 
                        sheet.write(row, col, report_item.strftime(date_fmt))
                    else:                               # Generic format
                        sheet.write(row, col, report_item)
                else:
                    sheet.write(row, col, '')

        book.close()
        

    # Reads a csv file and loads it into a memory using a 2dlist
    def read_csv(self, file_path: str, delimiter=","):
        with open(file_path, encoding="utf-8", newline='') as csvfile:
            csv_read_obj = csv.reader(csvfile, delimiter=delimiter)
            csv_read_lst = list(csv_read_obj)
            return csv_read_lst

    # Writes 2dlist to csv file
    def write_to_csv(self, file_path: str, data_lst: List[List], _delimiter=',', _quoteall=False):
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = None

            if (_quoteall):
                writer = csv.writer(file, delimiter=_delimiter, quoting=csv.QUOTE_ALL)
            else:
                writer = csv.writer(file, delimiter=_delimiter)

            writer.writerows(data_lst)
        return

    # Appends a row of data to file to a csv file
    def append_to_csv(self, file_path, data_lst: List[List], _delimiter=',', _quoteall=False):
        with open(file_path, "a", encoding="utf-8", newline="") as file:
            writer = None

            if (_quoteall):
                writer = csv.writer(file, delimiter=_delimiter, quoting=csv.QUOTE_ALL)
            else:
                writer = csv.writer(file, delimiter=_delimiter)

            writer.writerows(data_lst)
        return


    # Reads custom delimited file and returns 2d list of contents
    def read_delimited_file(self, file_path, fieldterminator, rowterminator):
        output_lst = []
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.readlines()

            for line in contents:
                rows = line.split(sep=rowterminator)
                last_row = len(rows) - 1
                for i in range(0, last_row):
                    row = rows[i]
                    output_lst.append(row.split(sep=fieldterminator))

        return output_lst


    # Writes 2dlist to file
    def write_delimited_file(self, file_path, data_lst, fieldterminator=',', rowterminator='\n'):
        data_lst = self.convert_lst_items_to_str(data_lst)
        with open(file_path, 'w', encoding='utf-8') as file:
            for i in range(0, len(data_lst)):
                items = data_lst[i]
                row = [(item or '') for item in items]
                data_lst[i] = row

            file.writelines(f'%s{rowterminator}' % fieldterminator.join(line) for line in data_lst)

    # Appends data from data_lst to specified file
    # If you wish to append data without appending the headers (0th row), use firstrow=1
    def append_delimited_file(self, file_path, data_lst, fieldterminator, rowterminator, firstrow=0):
        data_lst = self.convert_lst_items_to_str(data_lst)
        with open(file_path, 'a+', encoding='utf-8') as file:
            for i in range(firstrow, len(data_lst)):
                items = data_lst[i]
                row = [(item or '') for item in items]
                data_lst[i] = row

            file.writelines(f'%s{rowterminator}' % fieldterminator.join(line) for line in data_lst[firstrow:])

    # Writes string to file at file_path
    def append_string_to_file(self, file_path: str, data: str):
        with open(file_path, 'a') as file: #append mode 
            file.write(data)
    
    # Reads through a file and returns the lines in a list
    def read_file_as_lst(self, file_path: str):
        output_lst = []
        with open(file_path, 'r') as file:
            for line in file:
                line = line.replace('\n', '')
                line = line.replace('\t', '')
                line = line.replace('    ', '')
                output_lst.append(line)

        return output_lst

    # Saves a piece of data to a pickle file
    def save_pickle(self, file_path: str, data):
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
    
    # Loads and returns the data from a pickle file
    def load_pickle(self, file_path: str):
        with open(file_path, 'rb') as f:
            loaded_obj = pickle.load(f)
            return loaded_obj

    # Join two parts of a path and format it to use forward slashes
    def join_path(self, folder, name):
        return os.path.join(folder, name).replace('\\', '/')
    
    # JSON Loading and saving
    def load_json(self, file_path: str):
        with open(file_path, 'r') as read_file:
            data = json.load(read_file)
            return data
    
    def save_json(self, file_path, data: dict):
        with open(file_path, 'w') as write_file:
            json.dump(data, write_file)