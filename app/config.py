from configparser import ConfigParser

class Config:
    def __init__(self, config):
        self.mongo = config['MONGO']

def _loadConfig():
    config = ConfigParser()
    config.read('config.ini')
    return Config(config)

CONFIG = _loadConfig()
