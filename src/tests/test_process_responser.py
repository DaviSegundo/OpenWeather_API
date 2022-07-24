import unittest
from api.responses.responser_process import ProcessResponser

class TestProcessResponser(unittest.TestCase):
    """Class to test the correctness of process responder responses."""

    def test_get_response_success(self):
        """Tests the return in case of success of the request"""
        progress = 15.0

        process_responser = ProcessResponser()
        _, status_code = process_responser.get_by_id(progress)

        self.assertEqual(200, status_code)

    def test_get_response_not_found(self):
        """Tests the return in case of user identifier not found"""
        progress = None

        process_responser = ProcessResponser()
        _, status_code = process_responser.get_by_id(progress)

        self.assertEqual(404, status_code)

    def test_post_response_accepted(self):
        """Tests the return in case of accepted  request"""
        valid = True
        user_id = 1234

        process_responser = ProcessResponser()
        _, status_code = process_responser.post(check=valid, user_id=user_id)

        self.assertEqual(202, status_code)

    def test_post_response_exists(self):
        """Tests the return in case of already exists user identifier"""
        valid = False
        user_id = 1234

        process_responser = ProcessResponser()
        _, status_code = process_responser.post(check=valid, user_id=user_id)

        self.assertEqual(409, status_code)
