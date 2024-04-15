#!/bin/python3

"""
Given a specific API, returns information about the user's TODO list progress
"""

import requests
from sys import argv

def get_todo_list_progress(user_id):
    """
    Retrieves the user's TODO list progress from a specific API.
    
    Args:
        user_id (int): The ID of the user whose TODO list progress is to be retrieved.
        
    Returns:
        None: Prints the user's name, the number of completed tasks, and the list of completed task titles.
    """
    # Retrieve user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    
    # Retrieve user's TODO list
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    todo_response = requests.get(todo_url)
    todos = todo_response.json()
    
    # Filter completed tasks
    completed = [todo for todo in todos if todo.get("completed")]
    
    # Print user's progress
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                           len(completed), len(todos)))
    for todo in completed:
        print("\t {}".format(todo.get("title")))

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <user_id>")
    else:
        user_id = argv[1]
        get_todo_list_progress(user_id)
