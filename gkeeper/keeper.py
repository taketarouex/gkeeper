import os

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue


class Keeper(object):
    def __init__(self) -> None:
        self.keep = Keep()

    def login(self) -> None:
        user = os.environ.get('KEEP_USER')
        password = os.environ.get('KEEP_PASSWORD')
        if user is None or password is None:
            raise Exception('set KEEP_USER and KEEP_PASSWORD to environment')

        result = self.keep.login(user, password)
        if not result:
            raise ValueError('cant login')
        self._token = self.keep.getMasterToken()

    def _resume_keep(self) -> None:
        user = os.environ.get('KEEP_USER')
        self.keep.resume(email=user, master_token=self._token)

    def _fetch_list_by_title(self, title: str) -> Glist:
        glists = self.keep.find(query=title)
        try:
            glist = next(glists)
        except StopIteration:
            raise ValueError(f'no list title:{title}')

        return glist

    def add_item(self, list_name: str, item: str) -> None:
        self._resume_keep()
        glist = self._fetch_list_by_title(list_name)
        glist.add(item, False,
                  NewListItemPlacementValue.Bottom)
        self.keep.sync()
