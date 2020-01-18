from main import main
import pytest


@pytest.mark.large
def test_main(mocker):
    """depending on Google Keep"""
    # need to set the environ "KEEP_PASSWORD"
    request = mocker.Mock()
    request.get_json.return_value = {"item": "肉"}

    main(request)
