from logging import getLogger

from flask import Request

from gkeeper.keeper import Keeper

logger = getLogger(__name__)


def main(request: Request) -> None:
    request_json = request.get_json()
    if 'item' not in request_json:
        raise ValueError('request body doesnt include the key "item"')
    item = request_json['item']

    if 'list_name' not in request_json:
        raise ValueError('request body doesnt include the key "list_name"')
    list_name = request_json['list_name']

    try:
        logger.info("start gkeeper")
        keeper = Keeper()
        keeper.login()
        keeper.add_item(list_name=list_name, item=item)
        logger.info("end gkeeper")
    except Exception as e:
        logger.error(e.args[0])
        raise e
