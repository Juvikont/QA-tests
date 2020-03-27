import pytest
import random


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'), (-1, '-1'), (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('brewery_type', 'brewery_type'), ('', ''), (100, '100'), ('&', '&')])
def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
    res = api_client.post(
        path="/brewery",
        data={'brewery_type': input_title,
              'name': 'bar',
              'id': input_id
              }).json()
    assert res['brewery_type'] == output_title
    assert res['name'] == 'bar'
    assert res['id'] == output_id


# # Post's filter by User ID
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('id', [-1, 0])
def test_api_filtering(api_client, id):
    res = api_client.get(
        path="/brewery",
        params={'id': id}
    )
    # Empty data check
    assert res.json() == []


# Post's filter by User ID
# # https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('id, id_response', [(1, 1), (2, 2),(3,3),(5,5)])
def test_api_filtering(api_client, id, id_response):
    response = api_client.get(
        path="/brewery",
        params={'userId': id}
    )
    # Check's that random post has the right User ID
    random_post_number = random.randint(1, 10)
    assert response.json()[random_post_number]['userId'] == id_response

