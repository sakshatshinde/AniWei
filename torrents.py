from qbittorrent import Client
from aniwei_config import get_config_values

# https://pypi.org/project/python-qbittorrent/
qb = Client(get_config_values('client'))

print(qb.torrents(filter='downloading'))
