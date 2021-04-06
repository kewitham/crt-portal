from django.core import mail
from django.test import SimpleTestCase

from ..api.client import TMSClient
from . import TMSEmailBackend


class TMSEmailBackendTests(SimpleTestCase):

    def setUp(self):
        self.backend = TMSEmailBackend()

    def test_open_connection_is_a_tms_client(self):
        """Connection used for sending emails is a TMSClient instance"""
        self.backend.open()
        self.assertTrue(isinstance(self.backend.connection, TMSClient))
