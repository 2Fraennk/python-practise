import unittest

from src.properties import Props


class TestProperties(unittest.TestCase):
    def setUp(self):
        self.props = Props()

    def test_jira(self):
        self.assertIsNotNone(self.props.JIRA_UPDATE_TICKET, 'JIRA_UPDATE_TICKET not set')
        if self.props.JIRA_UPDATE_TICKET:
            self.assertIsNot(self.props.JIRA_URL, '', 'JIRA_URL not set')
            self.assertIsNot(self.props.JIRA_LOGIN_USER, '', 'JIRA_LOGIN_USER not set')
            self.assertIsNot(self.props.JIRA_LOGIN_TOKEN, '', 'JIRA_LOGIN_TOKEN not set')
            self.assertIsNot(self.props.JIRA_PROJECT_ESB_ID, '', 'JIRA_PROJECT_ESB_ID not set')


if __name__ == '__main__':
    unittest.main()
