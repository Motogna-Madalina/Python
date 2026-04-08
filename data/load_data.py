
import json

def load_json_file():
    with open('data/tasks.json', 'r', encoding='utf-8') as file:
        all_tasks = json.load(file)
        return all_tasks

#json file is a file format that is used to store data in a structured way.
# It is a text file that contains data in the form of key-value pairs.
# The json module in Python provides functions to read and write JSON files.
#The load_json_file() function opens the tasks.json file in read mode,
#reads the data from the file, and returns it as a Python dictionary.
# The encoding='utf-8' argument ensures that the file is read using the UTF-8 encoding, 
# which is important for handling special characters correctly.
#file is the file object that we want to read from.
#json.load() is a function that reads a JSON file and converts it into a Python object