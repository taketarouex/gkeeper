import pytest
import pytest_mock

from gkeeper.configs import ConfigParser


@pytest.fixture
def configparser(mocker: pytest_mock.mocker) -> ConfigParser:
    mock_load = mocker.patch('toml.load')
    mock_load.return_value = {
        'google': {
            'id': 'test'
        },
        'keep': {
            'list_name': 'test_list'
        }
    }
    configparser = ConfigParser()
    return configparser


class TestConfigParser(object):
    def test_google_config(self, configparser: pytest.fixture) -> None:
        google_config = configparser.google_config
        assert google_config.id == 'test'
