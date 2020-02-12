from flask import Request

from pytest_mock.plugin import MockFixture
from unittest.mock import MagicMock

from main import main


def test_main(mocker: MockFixture) -> None:
    request = mocker.MagicMock(spec=Request)
    test_item: str = 'meat'
    test_list_name: str = 'aaaa'
    request.get_json.return_value = {
        'list_name': test_list_name,
        'item': test_item
    }

    mocker.patch('main.ConfigParser')
    mock_keeper: MagicMock = mocker.patch('main.Keeper')

    main(request=request)

    mock_keeper().add.assert_called_with(
        list_name=test_list_name,
        item=test_item
    )
