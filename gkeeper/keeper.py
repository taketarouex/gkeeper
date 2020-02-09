import os
from typing import Generator

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue

from gkeeper.configs import ConfigParser, GoogleConfig, KeepConfig


class Keeper(object):
    def __init__(self, config_parser: ConfigParser) -> None:
        self.google_config: GoogleConfig = config_parser.google_config
        self.keep_config: KeepConfig = config_parser.keep_config
        self.keep = Keep()

    def _login(self, user: str) -> None:
        password = os.environ.get('KEEP_PASSWORD', 'password')
        result = self.keep.login(user, password)
        if not result:
            raise ValueError('cant login')

    def _fetch_list(self, title: str) -> Glist:
        glists: Generator[Glist, None, None] = self.keep.find(query=title)
        glist: Glist = next(glists)
        return glist

    def add(self, item: str) -> None:
        self._login(self.google_config.id)
        glist = self._fetch_list(self.keep_config.list_name)
        glist.add(item, False,
                  NewListItemPlacementValue.Bottom)
        self.keep.sync()
