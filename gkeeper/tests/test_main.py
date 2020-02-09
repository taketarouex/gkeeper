from pytest_mock.plugin import MockFixture
from unittest.mock import MagicMock

from main import main


def test_main(mocker: MockFixture) -> None:
    request = mocker.MagicMock()
    test_item: str = '肉'
    request.get_json.return_value = {'item': test_item}

    mocker.patch('main.ConfigParser')
    mock_keeper: MagicMock = mocker.patch('main.Keeper')

    main(request=request)

    mock_keeper().add.assert_called_with(item=test_item)
