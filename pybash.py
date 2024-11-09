import os
import toml

if os.path.exists("pybash.toml"):
    with open("pybash.toml", "r") as f:
        config = toml.load(f)

print(config)
