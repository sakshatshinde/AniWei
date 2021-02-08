import os
from colorama import init, Fore, Back, Style
from aniwei_config import manipulate_config

# Setting the anime library path
def set_anime_path():
    anime_path = input("Enter your anime path here! \n")

    if os.path.exists(anime_path) and os.path.isdir(anime_path):
        print(Fore.GREEN + 'Anime Library Found' + Style.RESET_ALL)
        manipulate_config('anime_path', anime_path)

    else:
        raise ValueError(Fore.RED + Back.YELLOW + 'Directory not found!' + Style.RESET_ALL)


# Checking OS compatibility
def os_check():
    if os.name == 'nt':         #nt -> Windows 
        # import explorer
        print(Fore.GREEN + ' Successful ' + Style.RESET_ALL)

    else:
        raise OSError(Fore.RED + Back.YELLOW + ' This only works on windows ' + Style.RESET_ALL)

# Setup Qbit-WEB
def qbit_web_setup(local_url:str,qb_username:str, qb_pass=None):
    manipulate_config('client', local_url)
    if qb_pass is None:
        qb_pass=''
    manipulate_config(qb_username, qb_pass)

    # qbit_web_setup('http://127.0.0.1:8080', 'admin')