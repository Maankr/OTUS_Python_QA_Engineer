import requests
import pytest

url = "https://api.openbrewerydb.org"


def test_get_breweries_list():
    response = requests.get(f"{url}/v1/breweries")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data, "Breweries list is empty"

@pytest.mark.parametrize("state", ["california", "new_york"])
def test_filter_by_state(state):
    r = requests.get(f"{url}/v1/breweries", params={"by_state": state})
    assert r.status_code == 200

    data = r.json()
    expected = state.replace("_", " ")

    assert data and all(
        b.get("state") and expected in b["state"].lower()
        for b in data
    )

@pytest.mark.parametrize("brewery_type", ["micro", "regional"])
def test_filter_by_type(brewery_type):
    response = requests.get(f"{url}/v1/breweries", params={"by_type": brewery_type})
    assert response.status_code == 200, \
        f"Unexpected status: {response.status_code}, body: {response.text}"

    data = response.json()

    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, f"No breweries returned for type '{brewery_type}'"

    for brewery in data:
        assert "brewery_type" in brewery, \
            f"brewery_type missing in response object: {brewery}"

        assert brewery["brewery_type"] == brewery_type, \
            f"Expected type '{brewery_type}', got '{brewery['brewery_type']}'"


def test_get_brewery_by_id():
    response = requests.get(f"{url}/v1/breweries")
    brewery_id = response.json()[0]["id"]

    assert response.status_code == 200,\
        f"Unexpected status code: {response.status_code}, body: {response.text}"
    data = response.json()

    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "Breweries list is empty"

    brewery_id = data[0]["id"]

    response = requests.get(f"{url}/v1/breweries/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id


def test_invalid_brewery_id():
    response = requests.get(f"{url}/v1/breweries/invalid-id")
    assert response.status_code == 404
