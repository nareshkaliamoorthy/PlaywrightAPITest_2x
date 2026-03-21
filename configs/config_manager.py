import os

import yaml

env = os.getenv("ENV","prod")

def load_config():
    with open(f"./configs/{env}.yml") as file:
        return yaml.safe_load(file)