from unittest import mock
from unittest.mock import call

from main import main


@mock.patch("builtins.print")
def test_main(mock_print):
    main()

    assert mock_print.mock_calls == [call("Hello World!")]
