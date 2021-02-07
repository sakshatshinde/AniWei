from configparser import ConfigParser
from colorama import init, Fore, Back, Style

# Manipulating the Config file for AnimeWei
def manipulate_config(key:str, value:str):
    config = ConfigParser()
    config.read('config.ini')
    # config.add_section('main')
    config.set('main', key, value)

    with open('config.ini', 'w') as f:  #f is an instance of opened File
        config.write(f)

# Retrieving values from config.ini
def get_config_values(section='main', key=None):
    config = ConfigParser()
    config.read('config.ini')

    if key is not None:
        # print(config[section][key])
        return config[section][key]
    
    if key is None:
        raise ValueError(Fore.RED + Back.WHITE + 
                        'Enter a key to retrieve a val from config.ini'
                        + Style.RESET_ALL)

# get_config_values('main')
