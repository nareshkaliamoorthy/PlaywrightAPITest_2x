from configs.config_manager import load_config


config = load_config()

def get_base_url(service_name):
    service = config["services"][service_name]
    base_url = service["base_url"]
    return base_url

def get_endpoint(service_name, endpoint_method):
    service = config["services"][service_name]
    endpoint = service["end_points"][endpoint_method]
    return endpoint

