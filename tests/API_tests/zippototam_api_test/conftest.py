import pytest
import requests


class APIClient:

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)


# Testing API: http://api.zippopotam.us/us/90210
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://api.zippopotam.us/us/90210",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
