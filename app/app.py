from typing import Dict
import requests


class App:
    def get(self, url: str) -> Dict[str, str]:
        resp: requests.Response = requests.get(url)
        resp.raise_for_status()
        return resp.json()
