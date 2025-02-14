from operator import attrgetter
from os import write

from rich import inspect, print

from model import Status, ToDo
from serialize import change_todo_from_json, del_1_from_json, read_json, write_json


def _take_new_id_todos():
    data = read_json()
    id = max(data, key=attrgetter("id")).id + 1 if data else 0
    return id


def create_todo(description: str):
    todo = ToDo(description=description)
    todo.id = _take_new_id_todos()
    write_json(todo)
    print(todo)


def delete_todo(id: int):
    del_1_from_json(id)
    print(f"{id} удален")


def change_todo(id: int, description: str, status: int):
    data = read_json()
    if description == "":
        description = [d for d in data if d.id == id][0].description
    if status == -1:
        status = [d for d in data if d.id == id][0].status.value
    change_todo_from_json(id, description, status=Status(status))
    data = read_json()
    print(*data)


def list_todo():
    data = read_json()
    print(*data)


def list_todo_by_status():
    data = read_json()
    new = sorted(data, key=lambda d: d.status.value)
    print(*new)
