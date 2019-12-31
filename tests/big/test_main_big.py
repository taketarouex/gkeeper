from main import main


def test_main(mocker):
    request = mocker.Mock()
    request.get_json.return_value = {"item": "肉"}

    main(request)
