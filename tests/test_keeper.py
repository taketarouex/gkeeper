import os
from unittest.mock import MagicMock

import pytest

from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue
from pytest_mock.plugin import MockFixture

from gkeeper.keeper import Keeper


class TestKeeper(object):
    @pytest.fixture
    def keeper(self) -> Keeper:
        return Keeper()

    def test_login(self, mocker: MockFixture, keeper: Keeper) -> None:
        def login(user: str, password: str) -> bool:
            if password != 'test_password':
                return False
            return True
        os.environ['KEEP_USER'] = 'test_user'
        os.environ['KEEP_PASSWORD'] = 'test_password'
        mock_login = mocker.patch('gkeepapi.Keep.login')
        mock_login.side_effect = login
        mock_getMasterToken = mocker.patch('gkeepapi.Keep.getMasterToken')
        mock_getMasterToken.return_value = 'test_token'
        keeper.login()
        mock_login.assert_called_with('test_user', 'test_password')
        assert keeper._token == 'test_token'

    def test_add_item(self, mocker: MockFixture, keeper: Keeper) -> None:
        os.environ['KEEP_USER'] = 'test_user'

        mock_resume = mocker.patch('gkeepapi.Keep.resume')

        mock_find = mocker.patch('gkeepapi.Keep.find')

        mock_glist = MagicMock(spec=Glist)
        mock_find.return_value = iter([mock_glist])

        mock_sync = mocker.patch('gkeepapi.Keep.sync')

        keeper._token = 'test_token'
        keeper.add_item(list_name='test_list', item='test_item')

        mock_resume.assert_called_once()

        mock_find.assert_called_with(query='test_list')
        mock_glist.add.assert_called_with('test_item', False,
                                          NewListItemPlacementValue.Bottom)
        mock_sync.assert_called_once()

        mock_find.return_value = iter([])
        with pytest.raises(ValueError):
            keeper.add_item(list_name='test_list', item='test_item')
