import requests
import pytest

url = "https://dog.ceo/api"


def test_get_all_breeds():
    response = requests.get(f"{url}/breeds/list/all")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("breed", ["cockapoo", "danish", "husky"])
def test_get_breed_images(breed):
    response = requests.get(f"{url}/breed/{breed}/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)


@pytest.mark.parametrize("breed", ["beagle", "greyhound"])
def test_get_random_image_by_breed(breed):
    response = requests.get(f"{url}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()["message"].startswith("https://")


def test_get_random_image():
    response = requests.get(f"{url}/breeds/image/random")
    assert response.status_code == 200


def test_nonexistent_breed():
    response = requests.get(f"{url}/breed/unknownbreed/images")
    assert response.status_code == 404
