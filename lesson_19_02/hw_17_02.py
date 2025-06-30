import requests
import pytest
from urllib.parse import quote, urlparse


@pytest.mark.hw17_02
def test_image():
    with open('sunrise.jpg', 'rb') as file:
        files = {'image': file}
        response_post = requests.post('http://127.0.0.1:8080/upload',files=files)

    assert  response_post.status_code == 201,  f'POST request status code is not 201, but {response_post.status_code}'
    data = response_post.json()
    assert data, 'Response JSON is empty'
    assert "image_url" in data, 'image_url is not in response'
    image_url = data["image_url"]
    assert image_url.startswith("http://127.0.0.1:8080/uploads/"), 'image_url has wrong path'
    assert image_url.endswith(('.jpg', '.jpeg', '.png')), "image_url should end with '.jpg', '.jpeg', '.png'"


    parsed_url = urlparse(image_url)
    filename = parsed_url.path.split('/')[-1]
    encoded_filename = quote(filename, safe="")

    response_get_text = requests.get(
        f'http://127.0.0.1:8080/image/{encoded_filename}',
        headers={"Content-Type": "text"}
    )
    assert response_get_text.status_code == 200, f'GET text request status code is not 200, but: {response_get_text.status_code}'
    assert "image_url" in response_get_text.json(), 'No "image_url" in GET text response'

    response_get_image = requests.get(
        f'http://127.0.0.1:8080/image/{encoded_filename}',
        headers={"Content-Type": "image"}
    )
    assert response_get_image.status_code == 200, f'GET image request status code is not 200, but: {response_get_image.status_code}'
    assert response_get_image.headers.get("Content-Type", "").startswith("image/"), 'Not an image response'
    assert response_get_image.content, "Empty image content"


    response_delete = requests.delete(f'http://127.0.0.1:8080/delete/{encoded_filename}')
    assert  response_delete.status_code == 200,  f'DELETE request status code is not 200, but {response_delete.status_code}'
    delete_data = response_delete.json()
    assert "image_url" in delete_data or "message" in delete_data, "DELETE response has no confirmation "
