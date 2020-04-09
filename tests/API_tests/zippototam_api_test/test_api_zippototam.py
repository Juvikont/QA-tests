from pprint import pprint

import pytest
import requests
# from tests.API_tests.zippototam_api_test.conftest import APIClient




def test_code_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


def test_json():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers['Content-Type'] == "application/json"


def test_country_us():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"


def test_location_places():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"


def test_places_number():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1


@pytest.mark.parametrize('place_name', ['Beverly Hills'])
def test_api_filtering(api_client, place_name):
    res = api_client.get(
        path="/",
        params={'place name': place_name}
    )
    print(res.json())
    #Empty data check
    assert res.json()[0]['place name'] == 'Beverly Hills'


# res = APIClient(base_address="http://api.zippopotam.us/us/90210")
# print(pprint(res.get(path='/').json()["places"][0]["place name"]))
