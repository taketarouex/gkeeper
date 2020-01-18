import pytest
from pytest_mock.plugin import MockFixture

from main import main


@pytest.mark.large
def test_main(mocker: MockFixture) -> None:
    """depending on Google Keep"""
    # need to set the environ "KEEP_PASSWORD"
    request = mocker.Mock()
    request.get_json.return_value = {"item": "肉"}

    main(request)
