import requests
import pytest

url = "https://api.openbrewerydb.org"


def test_get_breweries_list():
    response = requests.get(f"{url}/v1/breweries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("state", ["california", "new_york"])
def test_filter_by_state(state):
    response = requests.get(f"{url}/v1/breweries", params={"by_state": state})
    assert response.status_code == 200
    assert all(state.replace("_", " ") in b["state"].lower() for b in response.json())


@pytest.mark.parametrize("brewery_type", ["micro", "regional"])
def test_filter_by_type(brewery_type):
    response = requests.get(f"{url}/v1/breweries", params={"by_type": brewery_type})
    assert response.status_code == 200


def test_get_brewery_by_id():
    response = requests.get(f"{url}/v1/breweries")
    brewery_id = response.json()[0]["id"]

    response = requests.get(f"{url}/v1/breweries/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id


def test_invalid_brewery_id():
    response = requests.get(f"{url}/v1/breweries/invalid-id")
    assert response.status_code == 404
