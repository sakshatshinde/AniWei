import os 
from aniwei_config import get_config_values

# convert sizes into Human readable format
def sizeof_fmt(num, suffix='B') -> str:
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

# get size of the base folder
def collect_size_info(anime_path:str) -> str:
    total_size = 0
    for root, dirs, files in os.walk(anime_path):
        for _ in files:
            total_size += os.path.getsize(os.path.join(root, _))
    
    return sizeof_fmt(total_size)

    # Usage
    # print(collect_size_info(get_config_values(key='anime_path')))
