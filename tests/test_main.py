import os

import pytest
from gkeepapi import Keep
from gkeepapi.node import NewListItemPlacementValue
from pytest_mock.plugin import MockFixture

from main import _fetch_list, _login, main


def test_login(mocker: MockFixture) -> None:
    mock_keep = mocker.Mock()
    mock_keep.login = mocker.Mock()
    mock_keep.login.return_value = True
    os.environ['KEEP_PASSWORD'] = 'test'
    _login(mock_keep, 'test')
    mock_keep.login.assert_called_with("test", "test")

    mock_keep.login.return_value = False
    with pytest.raises(ValueError):
        _login(mock_keep, 'test')


def test_fetch_list(mocker: MockFixture) -> None:
    mock_keep = mocker.Mock()
    mock_keep.find = mocker.Mock()
    mock_glist = mocker.Mock()
    mock_keep.find.return_value = mocker.MagicMock(side_effect=[mock_glist])
    _fetch_list(mock_keep, '買い物')
    mock_keep.find.assert_called_with(query='買い物')


def test_main(mocker: MockFixture) -> None:
    request = mocker.Mock()
    request.get_json.return_value = {"item": "肉"}

    mock_login = mocker.patch("main._login")

    mock_fetch_list = mocker.patch("main._fetch_list")
    mock_glist = mocker.Mock()
    mock_fetch_list.return_value = mock_glist
    mock_add = mocker.Mock()
    mock_glist.add = mock_add

    mock_sync = mocker.patch.object(Keep, "sync")
    main(request)
    mock_login.assert_called()
    mock_fetch_list.assert_called()
    mock_add.assert_called_with('肉', False,
                                NewListItemPlacementValue.Bottom)
    mock_sync.assert_called()
