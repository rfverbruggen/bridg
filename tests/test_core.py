import bridg
import unittest


class CoreTestCase(unittest.TestCase):

    def setUp(self):
        self.app = bridg.create_app()
        self.app.testing = True
        self.app = self.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        assert result.data == b"Hello World!"
