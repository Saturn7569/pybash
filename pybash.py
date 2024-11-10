import os
import sys
import toml

from src.utils import get_config, get_alias, alias_exists
from src.parser import parse_command
from src.commands import commands

if os.path.exists("pybash.toml"):
    with open("pybash.toml", "r") as f:
        try:
            config = toml.load(f)
        except Exception as e:
            print(f"Error while loading config: '{e}'")
            sys.exit(1)


os.chdir(get_config(config, "base", "start_dir", "C:/"))

while True:
    currend_dir = os.getcwd().replace("\\", "/")
    inp_text = f"{currend_dir} {get_config(config, 'style', 'input_char', '>')} "

    inp = input(inp_text)
    parsed_txt = parse_command(inp)
    # print(parsed_txt)
    if inp == "exit":
        break

    if parsed_txt[0] in commands:
        commands[parsed_txt[0]](config, parsed_txt[1:])
        continue

    if (
        alias_exists(config, parsed_txt[0])
        and get_alias(config, parsed_txt[0]) in commands
    ):
        commands[get_alias(config, parsed_txt[0])](config, parsed_txt[1:])
        continue

    print(f"'{parsed_txt[0]}': Not a command")
