from flask import Request

from gkeeper.configs import ConfigParser
from gkeeper.keeper import Keeper


def main(request: Request) -> None:
    request_json = request.get_json()
    if 'item' not in request_json:
        raise ValueError('request body doesnt include the key "item"')
    item = request_json['item']

    if 'list_name' not in request_json:
        raise ValueError('request body doesnt include the key "list_name"')
    list_name = request_json['list_name']
    config_parser = ConfigParser()

    keeper = Keeper(config_parser=config_parser)
    keeper.add(list_name=list_name, item=item)
