def get_config(conf, section, name, default):
    if name not in conf:
        return default
    if name in conf[section]:
        return conf[section][name]
    return default


def alias_exists(conf, name):
    if "alias" not in conf:
        return False
    return name in conf["alias"]


def get_alias(conf, name):
    if "alias" not in conf:
        return None
    if name not in conf["alias"]:
        return None
    return conf["alias"][name]
