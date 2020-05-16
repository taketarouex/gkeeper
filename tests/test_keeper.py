import os
from unittest.mock import MagicMock

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue
from pytest_mock.plugin import MockFixture

from gkeeper.keeper import Keeper


class TestKeeper(object):
    def setup_method(self) -> None:
        self.test_user = 'test_user'
        self.test_list_name = 'test_list_name'
        self.test_password = 'test_password'

    def test_add(self, mocker: MockFixture) -> None:
        def login(user: str, password: str) -> bool:
            if password != self.test_password:
                return False
            return True
        keeper: Keeper = Keeper()
        mock_login: MagicMock = MagicMock(side_effect=login)
        mock_keep: MagicMock = MagicMock(spec=Keep)
        mock_keep.login = mock_login
        mock_glist: MagicMock = MagicMock(spec=Glist)
        mock_keep.find.return_value = iter([mock_glist])
        mocker.patch.object(keeper, 'keep', mock_keep)

        os.environ['KEEP_USER'] = self.test_user
        os.environ['KEEP_PASSWORD'] = self.test_password

        test_item = 'test'
        keeper.add(list_name=self.test_list_name, item=test_item)

        mock_login.assert_called_with(self.test_user, self.test_password)
        mock_keep.find.assert_called_with(query=self.test_list_name)
        mock_glist.add.assert_called_with(test_item, False,
                                          NewListItemPlacementValue.Bottom)
        mock_keep.sync.assert_called_once()
