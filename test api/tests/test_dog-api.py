import requests
import pytest

url = "https://dog.ceo/api"


def test_get_all_breeds():
    r = requests.get(f"{url}/breeds/list/all")
    assert r.status_code == 200

    data = r.json()
    assert data["status"] == "success"
    assert isinstance(data.get("message"), dict)
    assert data["message"], "Breeds list is empty"


@pytest.mark.parametrize("breed", ["cockapoo", "danish", "husky"])
def test_get_breed_images(breed):
    r = requests.get(f"{url}/breed/{breed}/images")
    assert r.status_code == 200

    data = r.json()
    assert data["status"] == "success"

    images = data["message"]
    assert isinstance(images, list)
    assert images, f"No images returned for breed '{breed}'"


@pytest.mark.parametrize("breed", ["beagle", "greyhound"])
def test_get_random_image_by_breed(breed):
    r = requests.get(f"{url}/breed/{breed}/images/random")
    assert r.status_code == 200

    data = r.json()
    assert data["status"] == "success"

    image_url = data["message"]
    assert image_url.startswith("https://")
    assert breed in image_url, \
        f"Returned image does not match breed '{breed}': {image_url}"

def test_get_random_image():
    r = requests.get(f"{url}/breeds/image/random")
    assert r.status_code == 200

    data = r.json()
    assert data["status"] == "success"

    image_url = data["message"]
    assert isinstance(image_url, str)
    assert image_url.startswith("https://images.dog.ceo/")


def test_nonexistent_breed():
    response = requests.get(f"{url}/breed/unknownbreed/images")
    assert response.status_code == 404
