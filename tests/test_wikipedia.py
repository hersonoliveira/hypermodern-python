from unittest.mock import Mock

from click import ClickException
import pytest

from hypermodern_python import wikipedia
from hypermodern_python.models import Page
from hypermodern_python.wikipedia import random_page


def test_random_page_returns_page(mock_requests_get):
    page = random_page()
    assert isinstance(page, Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(ClickException):
        wikipedia.random_page()
