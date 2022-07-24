from .mock_data import MOCK_RETURN_API, MOCK_URL_API_SUCCESS

def mocked_requests_get(*args):
    class MockResponse:
        def __init__(self, status_code: int, json_data: dict):
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data
    if args[0] == MOCK_URL_API_SUCCESS:
        return MockResponse(200, MOCK_RETURN_API)

    return MockResponse(404, {'cod': '404', 'message': 'city not found'})