import pytest
from pytest_mock.plugin import MockFixture
from unittest.mock import MagicMock, PropertyMock

from gkeepapi import Keep
from gkeepapi.node import List as Glist
from gkeepapi.node import NewListItemPlacementValue

from gkeeper.keeper import Keeper
from gkeeper.configs import ConfigParser, GoogleConfig


class TestKeeper(object):
    def setup_method(self) -> None:
        self.test_id = 'test_id'
        self.test_list_name = 'test_list_name'
        self.test_password = 'test_password'

    @pytest.fixture
    def config(self, mocker: MockFixture) -> Keeper:
        mock_config: MagicMock = mocker.MagicMock(spec=ConfigParser)
        mock_google_config: MagicMock = mocker.MagicMock(spec=GoogleConfig)
        type(mock_google_config).id = PropertyMock(
            return_value=self.test_id)

        type(mock_config).google_config = PropertyMock(
            return_value=mock_google_config)
        return mock_config

    def test_add(self, mocker: MockFixture,
                 config: MockFixture) -> None:
        def login(user: str, password: str) -> bool:
            if password != self.test_password:
                return False
            return True
        keeper: Keeper = Keeper(config_parser=config)
        mock_login: MagicMock = MagicMock(side_effect=login)
        mock_keep: MagicMock = MagicMock(spec=Keep)
        mock_keep.login = mock_login
        mock_glist: MagicMock = MagicMock(spec=Glist)
        mock_keep.find.return_value = iter([mock_glist])
        mocker.patch.object(keeper, 'keep', mock_keep)

        mock_environ = mocker.patch('os.environ.get')
        mock_environ.return_value = self.test_password

        test_item = 'test'
        keeper.add(list_name=self.test_list_name, item=test_item)

        mock_login.assert_called_with(self.test_id, self.test_password)
        mock_keep.find.assert_called_with(query=self.test_list_name)
        mock_glist.add.assert_called_with(test_item, False,
                                          NewListItemPlacementValue.Bottom)
        mock_keep.sync.assert_called_once()
