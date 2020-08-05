import bridg
import unittest


class CoreTestCase(unittest.TestCase):
    """Core test case."""

    def setUp(self):
        """set up function."""
        self.app = bridg.create_app()
        self.app.testing = True
        self.app = self.app.test_client()

    def test_home(self):
        """Test the home page."""
        result = self.app.get('/')
        assert result.data == b"Hello World!"
