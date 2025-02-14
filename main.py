from ClI import ToDoCLI
from model import Status, ToDo
from serialize import read_json, write_json
from console_print import console_print


def main():
    """
    Main function
    """
    ToDoCLI().cmdloop()


if __name__ == "__main__":
    main()
