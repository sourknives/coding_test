""" Testing file to test all three methods of jsonplaceholder.py via pytest"""
import pytest
from jsonplaceholder import JsonPlaceholder

jp = JsonPlaceholder()


@pytest.mark.parametrize("test_method,test_resource,test_return_type, expected_response", [
    ("get", "posts", "full", "<Response [200]>"),
    ("get", "posts/8/comments", "full", "<Response [200]>"),
    ("get", "users", "full", "<Response [200]>"),
    ("put", "posts/12", "full", "<Response [200]>"),
    ("get", "posts/101", "full", "<Response [404]>"),
    ("post", "posts/25", "full", "Unsupported method: api_request supports GET & PUT"),
    # Test for ValueError on unexpected return_type
    ("get", "posts", "foo", "Unsupported return type: Valid options are json, raw, and full.")
])
def test_api_request(test_method, test_resource, test_return_type, expected_response):
    """
    Parameterizing test inputs to test various different scenarios for api_request

    For brevity, return_type is being limited to 'full' to return the entire
    response object allowing the ability to verify the top level
    Response (or ValueError when applicable).
    """
    assert str(jp.api_request(method=test_method, resource=test_resource,
                              return_type=test_return_type)) == str(expected_response)


@pytest.mark.parametrize("test_resource,test_resource_number, expected_len", [
    # Testing all resource collection, expected len is 10 (returns a list of 10 user dicts)
    ("users", None, 10),
    # Testing a single post collection, expected len is 8 (return a dict with 8 key/value pairs)
    ("posts", 25, 4),
    # Testing an invalid resource, expected len is 0 (returns an empty dict)
    ("foo", None, 0),
    # Testing an invalid single resource, expected len is 0 (returns an empty dict)
    ("posts", 101, 0)
])
def test_get(test_resource, test_resource_number, expected_len):
    """
    Parameterizing test inputs for JsonPlaceholder.get()
    in order to test various different scenarios.

    For variety, using return_type of 'json' to verify the dict length of the response
    """
    assert len(jp.get(resource=test_resource, resource_number=test_resource_number)) == expected_len


@pytest.mark.parametrize("test_resource, test_resource_number, test_data, expected", [
    ("posts", 5, {}, 5),
    ("users", 3, {}, 3),
    ("posts", None, {}, None),
    # Confirming that a PUT request to comments is not successful
    ("posts/8/comments", None, {}, None)
])
def test_put(test_resource, test_resource_number, test_data, expected):
    """
    Parameterizing test inputs for JsonPlaceholder.put()
    in order to test various different scenarios.

    For brevity, all data will be an emtpy dict '{}'

    NOTE: PUT only works on the /posts/# level.
    All others will return and empty dict, so .get('id') will return None
    """
    assert jp.put(resource=test_resource, resource_number=test_resource_number,
                  data=test_data).get('id') == expected
