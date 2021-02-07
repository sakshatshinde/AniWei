from configparser import ConfigParser

# Manipulating the Config file for AnimeWei
def manipulate_config(key:str, value:str):
    config = ConfigParser()
    config.read('config.ini')
    # config.add_section('main')
    config.set('main', key, value)

    with open('config.ini', 'w') as f:  #f is an instance of opened File
        config.write(f)