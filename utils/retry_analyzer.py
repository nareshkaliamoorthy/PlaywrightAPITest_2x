import time

RETRY_STATUS = [429, 500, 501, 502, 503]

def retry_request(func, retries=3):
    print(type(retries))

    for attempt in range(retries):
        response = func()

        if response.status not in RETRY_STATUS:
            print(response)
            return response

        if response.status == 429:
            retry_after_time = response.headers.get("Retry-After",2)
            wait_time = int(retry_after_time)
        else:
            print(response)
            wait_time = 2

        print(f"Attemp {attempt} Failed: Retrying after {wait_time} seconds..")
        time.sleep(wait_time)
    
    return response



