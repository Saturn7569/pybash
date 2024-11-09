import os


def cmd_clear(_):
    os.system("cls")


commands = {"clear": cmd_clear}
