import configparser


def read_config(key: str) -> str:
    config = configparser.ConfigParser()
    config.read(r'C:\python_projects\weatherbot\configs\config.ini')
    value = config['keys'][key]
    return value
