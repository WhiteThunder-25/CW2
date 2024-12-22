from unittest.mock import patch

from src.hh_api import HeadHunterAPI


@patch("requests.get")
def test_head_hunter_api_requests(test_requests_api):

    obj_api = HeadHunterAPI()
    assert type(obj_api) is HeadHunterAPI
