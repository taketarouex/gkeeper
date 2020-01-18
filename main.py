import os
from typing import Generator

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue

from lib.configs import ConfigParser


def main(request):
    request_json = request.get_json()
    if 'item' not in request_json:
        raise ValueError('request body doesnt include the key "item"')
    item = request_json['item']

    config_parser = ConfigParser()
    google_config = config_parser.google_config
    keep_config = config_parser.keep_config

    keep = Keep()
    _login(keep, google_config.id)
    glist = _fetch_list(keep, keep_config.list_name)
    glist.add(item, False,
              NewListItemPlacementValue.Bottom)
    keep.sync()


def _login(keep: Keep, user: str):
    password = os.environ.get('KEEP_PASSWORD', 'password')
    result = keep.login(user, password)
    if not result:
        raise ValueError('cant login')


def _fetch_list(keep: Keep, title: str) -> Glist:
    glists: Generator[Glist, None, None] = keep.find(query=title)
    glist = next(glists)
    return glist
