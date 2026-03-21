import allure
import pytest

from services.typicod_service import Typicod_Service
from utils.csv_utils import get_csv_data
from utils.endpoint_helper import get_endpoint
from utils.json_parser import get_json_data
from utils.xlsx_utils import get_xlsx_data

post_payload = {
  "title": "Your Post Title",
  "body": "The main content of your post.",
  "userId": 1
}

@pytest.mark.api
def test_typicod_get_api_response(api_context):
    with allure.step("Initializing the API"):
        api = Typicod_Service(api_context)
        endpoint = get_endpoint("typicod_service","get")
    with allure.step("Sending API Request"):
        response = api.get_request(endpoint)
        print(response.json())
    
@pytest.mark.api
@pytest.mark.parametrize("test_data",get_json_data("C:\\Users\\DELL\\Downloads\\json_test_data.json"))
def test_typicod_post_api_response(api_context, test_data):
    with allure.step("Initializing the API"):
        api = Typicod_Service(api_context)
        end_point = get_endpoint("typicod_service","post")
    with allure.step("Sending API Request"):
        response = api.post_request(end_point,test_data["request_payload"])
        print(response.json())
        print(response.status)
        print(response.body())

@pytest.mark.api
@pytest.mark.parametrize("data",get_csv_data("C:\\Users\\DELL\\Downloads\\api_payloads_v2.csv"))
def test_typicod_multi_post_api_response(api_context, data):
    with allure.step("Initializing the API"):
        api = Typicod_Service(api_context)
        end_point = get_endpoint("typicod_service","post")
    with allure.step("Sending POST Request"):
        response = api.post_request(end_point,data["request_payload"])
        print(response.json())
        print(response.status)
        print(response.body())

@pytest.mark.api
@pytest.mark.parametrize("data",get_xlsx_data("C:\\Users\\DELL\\Downloads\\api_payloads_XL.xlsx"))
def test_typicod_xlsx_api_response(api_context, data):
    with allure.step("Initializing the API"):
        api = Typicod_Service(api_context)
        end_point = get_endpoint("typicod_service","post")
    with allure.step("Sending POST Request"):
        response = api.post_request(end_point,data["request_payload"])
        print(response.json())
        print(response.status)
        print(response.body())


    

    
    