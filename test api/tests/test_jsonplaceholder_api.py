import requests
import pytest

url = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{url}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(post_id):
    response = requests.get(f"{url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.parametrize("user_id", [1, 2])
def test_filter_posts_by_user(user_id):
    response = requests.get(f"{url}/posts", params={"userId": user_id})
    assert response.status_code == 200
    assert all(post["userId"] == user_id for post in response.json())


def test_create_post():
    payload = {"title": "test", "body": "body", "userId": 1}
    response = requests.post(f"{url}/posts", json=payload)
    assert response.status_code == 201


def test_nonexistent_post():
    response = requests.get(f"{url}/posts/9999")
    assert response.status_code == 404
