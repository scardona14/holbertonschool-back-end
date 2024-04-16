#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""

import requests
from sys import argv


def get_todo_list_progress(user_id):
    """
    Retrieves the user's TODO list progress from a specific API.
    """
    # Retrieve user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    # Retrieve user's TODO list
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format
    (user_id)
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Filter completed tasks
    completed = [todo for todo in todos if todo.get("completed")]

    # Print user's progress


todo_response = requests.get(todo_url)

todos = todo_response.json()

completed = [todo for todo in todos if todo.get("completed")]

print(f"Employee {user['name']}done with task({len(completed)}/{len(todos)}):")
for todo in completed:
    print("\t {}".format(todo.get("title")))


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python3 script.py <user_id>")
    else:
        user_id = argv[1]
        get_todo_list_progress(user_id)
