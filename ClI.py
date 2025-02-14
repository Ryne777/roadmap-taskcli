import cmd

from command import *


class ToDoCLI(cmd.Cmd):
    prompt = "todo-cli>> "
    intro = 'Welcome to ToDoCLI. Type "help" for available commands.'

    def __init__(self):
        super().__init__()

    def do_add(self, description: str):
        """Добавьте TODO"""
        create_todo(description=description)

    def do_list(self, line):
        """Вывести список TODO"""
        list_todo()

    def do_list_by_sts(self):
        """вывести список по статусу"""
        list_todo_by_status()

    def do_del(self, id: int):
        """удалить"""
        delete_todo(id)

    def do_chg_sts(self, arg: str):
        """Изменить статус"""
        id, status = arg.split()
        change_todo(int(id), "", int(status))

    def do_chg_des(self, arg: str):
        """Изменить описание"""
        id, des = arg.split()
        change_todo(int(id), des, -1)

    def do_q(self, line):
        """Выйти из CLI."""
        return True

    def postcmd(self, stop, line):
        print()  # Добавьте пустую строку для лучшей читабельности
        return stop


if __name__ == "__main__":
    ToDoCLI().cmdloop()
