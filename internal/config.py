import os
from dotenv import dotenv_values


def load_config():
    # TODO load environment specific configs
    config = dotenv_values(".env")
    
    return config

config = load_config()