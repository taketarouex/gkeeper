from flask import Request

from gkeeper.configs import ConfigParser
from gkeeper.keeper import Keeper


def main(request: Request) -> None:
    request_json = request.get_json()
    if 'item' not in request_json:
        raise ValueError('request body doesnt include the key "item"')
    item = request_json['item']

    config_parser = ConfigParser()

    keeper = Keeper(config_parser=config_parser)
    keeper.add(item=item)
