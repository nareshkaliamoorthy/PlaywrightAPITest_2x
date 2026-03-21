from playwright.sync_api import APIRequestContext

from utils.endpoint_helper import get_base_url, get_endpoint
from utils.retry_analyzer import retry_request


class Typicod_Service:

    def __init__(self, request_context:APIRequestContext):
        self.request = request_context
        self.base_url = get_base_url("typicod_service")

    def get_request(self, endpoint):
        #return self.request.get(f"{base_url}{endpoint}")
        return retry_request(lambda: self.request.get(f"{self.base_url}{endpoint}"))
    
    def post_request(self, endpoint, payload):
        return retry_request(lambda: self.request.post(f"{self.base_url}{endpoint}",data=payload))