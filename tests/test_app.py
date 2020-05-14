from typing import Any, Dict
from unittest.mock import Mock
from _pytest.monkeypatch import MonkeyPatch
import pytest
import requests
from app.app import App

fake_resp: Dict[str, str] = {'hello': 'world'}


@pytest.fixture
def app() -> App:
    return App()


class TestApp:
    def test_get_with_handmade_mock(
        self, app: App, monkeypatch: MonkeyPatch
    ) -> None:
        class MockResponse:
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                pass

            def raise_for_status(self, *args: Any, **kwargs: Any) -> None:
                pass

            def json(self) -> Dict[str, str]:
                return fake_resp

        monkeypatch.setattr(requests, 'get', MockResponse)
        assert app.get('http://afnor.org') == fake_resp

    def test_get_with_unittest_mock(
        self, app: App, monkeypatch: MonkeyPatch
    ) -> None:
        mock: Mock = Mock()
        mock.return_value.json = lambda: fake_resp  # OR mock.return_value.json.return_value = fake_resp
        monkeypatch.setattr(requests, 'get', mock)
        assert app.get('http://afnor.org') == fake_resp
