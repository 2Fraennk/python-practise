import unittest

from src.properties import Props


class TestProperties(unittest.TestCase):
    def setUp(self):
        self.props = Props()

    def test_stage(self):
        self.assertIsNotNone(self.props.stage, 'stage not set')

    def test_url(self):
        self.assertIsNotNone(self.props.url, 'url not set')

    def test_amq_user(self):
        self.assertIsNotNone(self.props.ACTIVEMQ_USER, 'ACTIVEMQ_USER not set')

    def test_amq_pwd(self):
        self.assertIsNotNone(self.props.ACTIVEMQ_PASSWORD, 'ACTIVEMQ_PASSWORD not set')

    def test_headless(self):
        self.assertIsNotNone(self.props.HEADLESS, 'HEADLESS not set')


if __name__ == '__main__':
    unittest.main()
