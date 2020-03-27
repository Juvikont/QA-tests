import pytest
import random

test_users = [(1, "Leanne Graham", 'Bret'), (2, "Ervin Howell", 'Antonette'), (3, "Clementine Bauch", 'Samantha')]


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'), (-1, '-1'), (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'), ('', ''), (100, '100'), ('&', '&')])
def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
    res = api_client.post(
        path="/posts",
        data={'title': input_title,
              'body': 'bar',
              'userId': input_id
              }).json()
    assert res['title'] == output_title
    assert res['body'] == 'bar'
    assert res['userId'] == output_id


# # Post's filter by User ID
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId', [-1, 0])
def test_api_filtering(api_client, userId):
    res = api_client.get(
        path="/posts",
        params={'userId': userId}
    )
    # Empty data check
    assert res.json() == []


# Post's filter by User ID
# # https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2), (3, 3), (5, 5)])
def test_api_filtering(api_client, userId, userId_in_response):
    response = api_client.get(
        path="/posts",
        params={'userId': userId}
    )
    # Check's that random post has the right User ID
    random_post_number = random.randint(1, 10)
    assert response.json()[random_post_number]['userId'] == userId_in_response


@pytest.mark.parametrize('userid, expected_name, expected_username', test_users)
def test_check_name(api_client, userid, expected_name, expected_username):
    response = api_client.get(
        path=f'/users/{userid}',

    )
    response_body = response.json()
    assert response_body['name'] == expected_name
    assert response_body['username'] == expected_username
