import os
from typing import Generator

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue


class Keeper(object):
    def __init__(self) -> None:
        self.keep = Keep()

    def _login(self) -> None:
        user = os.environ.get('KEEP_USER')
        password = os.environ.get('KEEP_PASSWORD')
        if user is None or password is None:
            raise Exception('set user and password to environment')

        result = self.keep.login(user, password)
        if not result:
            raise ValueError('cant login')

    def _fetch_list(self, title: str) -> Glist:
        glists: Generator[Glist, None, None] = self.keep.find(query=title)
        glist: Glist = next(glists)
        return glist

    def add(self, list_name: str, item: str) -> None:
        self._login()
        glist = self._fetch_list(title=list_name)
        glist.add(item, False,
                  NewListItemPlacementValue.Bottom)
        self.keep.sync()
