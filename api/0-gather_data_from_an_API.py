#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()
    todo_all_employees = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todo_all_employees[user_id] = []
        for todo in todos:
            if user_id == todo.get("userId"):
                todo_all_employees[user_id].append({
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                })