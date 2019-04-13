import yaml

def load_config(config_path):
    with open(config_path, "r") as fd:
        return yaml.full_load(fd)