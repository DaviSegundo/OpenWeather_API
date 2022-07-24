import unittest
from mongoengine import connect, disconnect
from api.controllers.controller_process import ProcessController
from models.process import Process


class TestProcessController(unittest.TestCase):
    """Class to test process controller functionality."""

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost', uuidRepresentation='standard')

    @classmethod
    def tearDownClass(cls):
       disconnect()

    def test_create_new_process_success(self):
        """Test the successful creation of a new process"""
        process_controller = ProcessController()
        response = process_controller.create_new_process(1234)

        self.assertTrue(response)

    def test_create_new_process_exists(self):
        """Tests the creation of a process that already exists"""
        process = Process(user_id=4567)
        process.save()

        process_controller = ProcessController()
        response = process_controller.create_new_process(4567)

        self.assertFalse(response)

    def test_check_progress_success(self):
        """Tests whether the data collection progress acquisition was a success"""
        process = Process(user_id=4567)
        process.save()

        process_controller = ProcessController()
        response = process_controller.check_progress_process(4567)

        self.assertEqual(float, type(response))

    def test_check_progress_not_exist(self):
        """Tests if the check looked for a process that had not been started"""
        process_controller = ProcessController()
        response = process_controller.check_progress_process(4567)

        self.assertIsNone(response)

