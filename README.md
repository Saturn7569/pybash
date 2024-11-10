# PyBash

A python bash toy I made because I was bored...

## Installing

First clone this repository into you computer.
You need to have python installed because I don't have a stable build yet
Now cd into the directory and run these commands:

```sh
pip install -r requirements.txt
```

This will install the [`uv`](https://github.com/astral-sh/uv) package and `toml` to open the config file

### Running

Now that you have [`uv`](https://github.com/astral-sh/uv) installed you can run the `pybash.py` file with

```sh
uv run pybash.py
```

## Some commands

### Sudo

In PyBash the `sudo` command lets you run a normal terminal command. For example:

```sh
sudo python
```

This will start the python cli in PyBash.

You can even start pybash **inside** of pybash by cding into the directory you have pybash cloned and running

```sh
sudo uv run pybash.py
```

**Note**: _running `sudo cd` will not actually let you cd into a different directory_

## Configuring PyBash

PyBash lets you configure it however you want.
The configuration is just stored in a toml file in the directory you cloned pybash into.

To start configuring it create the `pybash.toml` file in the cloned directory and open it in a text editor

```sh
touch pybash.toml
```

### Base Config

In the base config you can configure your starting directory like so:

```toml
[base]
start_dir = "some/path" # start directory
```

Running pybash now, you will see this:

```
some/path >
```

### Styling PyBash

Currently, PyBash doesn't have much style configuration but you can change the input cursor like so:

```toml
[style]
input_char = "$"
```

If you run uv now it will look like this:

```
some/path $
```

You can add new lines in the `input_char` and it will look like this

```toml
[style]
input_char = "\n$"
```

PyBash:

```
some/path
$
```

### Full config

```toml
[base]
start_dir = "some/path" # start directory

[style]
input_char = "$"
```
