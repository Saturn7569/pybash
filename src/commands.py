import os

def cmd_clear(*_):
    os.system("cls")

def cmd_ls(*_):
    files = os.listdir()
    files.sort()
    for file in files:
        if os.path.isdir(file):
            print(f"{file}/")
            continue
        print(file)

def cmd_sudo(_, args):
    os.system(" ".join(args))

def cmd_cd(_, args):
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        print(f"'{args[0]}': Not a directory")
    except Exception as e:
        print(f"'cd': '{e}'")

commands = {"clear": cmd_clear, "ls": cmd_ls, "cd": cmd_cd, "sudo": cmd_sudo}