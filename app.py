import os
from typing import Tuple

from flask import Flask, request
from werkzeug.exceptions import BadRequest

from gkeeper.keeper import Keeper

app = Flask(__name__)
keeper = Keeper()
keeper.login()


@app.route('/api/list/<list_name>/item', methods=['POST'])
def post_item(list_name: str) -> Tuple[str, int]:
    item = request.json['item']
    try:
        keeper.add_item(list_name=list_name, item=item)
    except ValueError as e:
        raise BadRequest(e.args[0])
    return f'Success to add {item} to {list_name}', 200


@app.route('/api/health', methods=['GET'])
def health() -> Tuple[str, int]:
    return 'OK', 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
