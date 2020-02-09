import dataclasses
from typing import Any, MutableMapping

import toml


@dataclasses.dataclass(frozen=True)
class GoogleConfig:
    id: str


@dataclasses.dataclass(frozen=True)
class KeepConfig:
    list_name: str


class ConfigParser(object):
    def __init__(self) -> None:
        config: MutableMapping[str, Any] = toml.load(
            open('configs/config.toml'))
        self.google_config: GoogleConfig = GoogleConfig(config['google']['id'])
        self.keep_config: KeepConfig = KeepConfig(config['keep']['list_name'])
