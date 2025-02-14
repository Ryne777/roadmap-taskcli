from datetime import datetime
import json
from model import Status, ToDo
from rich import print


def _todo_to_dict(todo: ToDo):
    return {
        "id": todo.id,
        "description": todo.description,
        "status": todo.status.value,
        "start_at": todo.start_at.strftime("%Y-%m-%d, %H:%M:%S.%f"),
        "update_at": todo.update_at.strftime("%Y-%m-%d, %H:%M:%S.%f"),
    }


def write_json(todo: ToDo):
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if str(todo.id) in data:
        print("этот id уже есть")
        return
    data[todo.id] = _todo_to_dict(todo)
    with open("todo.json", "w") as f:
        json.dump(data, f)


def read_json():
    todos: list[ToDo] = []
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if not data:
        print("No todos found.")
        todos = []
    for _, details in data.items():

        todo = ToDo(
            details["description"],
            Status(details["status"]),
            datetime.strptime(details["start_at"], "%Y-%m-%d, %H:%M:%S.%f"),
            datetime.strptime(details["update_at"], "%Y-%m-%d, %H:%M:%S.%f"),
        )
        todo.id = details["id"]
        todos.append(todo)

    return todos


def del_1_from_json(id: int):
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    if str(id) in data:
        data.pop(str(id))
    else:
        print("id not found")
    with open("todo.json", "w") as f:
        json.dump(data, f)


def change_todo_from_json(id: int, description: str, status: Status):
    try:
        with open("todo.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    data[str(id)]["description"] = description
    data[str(id)]["status"] = status.value
    data[str(id)]["update_at"] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f")
    with open("todo.json", "w") as f:
        json.dump(data, f)
