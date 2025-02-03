import pytest
import requests

import source.service as service

import unittest.mock as mock


@mock.patch("source.service.get_from_db")
def test_get_from_db(id_from_db):
    id_from_db.return_value = "Mocked Google"

    name = service.get_from_db(1)

    # Replace "Mocked xxxxxx" with "Mocked Google" to passed
    assert name == "Mocked xxxxxx"


# Test case to mock the API response and verify the function's behavior
@mock.patch("requests.get")
def test_get_users_from_api(mock_get):
    # Create a mock response object
    mock_response = mock.Mock()

    # Set the status code of the mock response to 200 (successful response)
    mock_response.status_code = 200

    # Define the JSON data that should be returned by the mock response
    mock_response.json.return_value = {"id": 1, "name": "Leanne Graham"}

    # Mock the requests.get method to return the mock response
    mock_get.return_value = mock_response

    # Call the function under test, which should now use the mocked response
    data = service.get_users_from_api()

    # Assert that the function returns the expected data
    assert data == {"id": 1, "name": "Leanne Graham"}


# Test case to simulate an error response from the API
@mock.patch("requests.get")
def test_get_users_from_api_error(mock_get):
    # Create a mock response object to simulate a failed API request
    mock_response = mock.Mock()

    # Set the status code of the mock response to 400 (bad request, error case)
    mock_response.status_code = 400

    # Mock the requests.get method to return the mock response
    mock_get.return_value = mock_response

    # Use pytest's.raises to assert that an HTTPError is raised when the API returns an error
    with pytest.raises(requests.HTTPError):
        # Call the function under test, which should raise an HTTPError due to the 400 status code
        service.get_users_from_api()
