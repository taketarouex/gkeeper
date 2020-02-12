import dataclasses
from typing import Any, MutableMapping

import toml


@dataclasses.dataclass(frozen=True)
class GoogleConfig:
    id: str


class ConfigParser(object):
    def __init__(self) -> None:
        config: MutableMapping[str, Any] = toml.load(
            open('configs/config.toml'))
        self.google_config: GoogleConfig = GoogleConfig(config['google']['id'])
