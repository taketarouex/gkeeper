from gkeepapi import Keep
from gkeepapi.node import NewListItemPlacementValue, List as Glist
import os
from typing import Generator


def main(request):
    request_json = request.get_json()
    if 'item' not in request_json:
        raise ValueError('request body doesnt include the key "item"')
    item = request_json['item']
    keep = Keep()
    _login(keep, 'the.saki72@gmail.com')
    glist = _fetch_list(keep, '買い物')
    glist.add(item, False,
              NewListItemPlacementValue.Bottom)
    keep.sync()


def _login(keep: Keep, user: str):
    password = os.environ.get('KEEP_PASSWORD', 'password')
    result = keep.login(user, password)
    if not result:
        raise ValueError('cant login')


def _fetch_list(keep: Keep, title: str) -> Glist:
    glistlist: Generator[Glist] = keep.find(query=title)
    glist = next(glistlist)
    return glist
