from datetime import date
from properties import Props
from jira import JIRA

import logging


class MyJira:
    logger = logging.getLogger(__name__)
    date_today = date.today()

    logger.debug("START : vars initialized. Let me do the work for you...")



    def init_jira_connection(self):
        jira_client = JIRA(server=Props.JIRA_URL,
                           token_auth=Props().JIRA_LOGIN_TOKEN,
                           )
        return jira_client

    def get_current_dlq_ticket(self, jiraclient):
        ticket = jiraclient.search_issues('project=ESB and summary~"jmx-activemq-dlq" and assignee = currentUser() and createdDate > startOfDay()', maxResults=1)
        try:
            if ticket[0].key != "":
                ticket_key = ticket[0].key
                self.logger.debug(f"Ticket {ticket_key} found")
                return ticket_key
            else:
                self.logger.error(f"Ticket key not set.")
                raise Exception("Ticket key not set.")
        except:
            self.logger.error(f"There is no current-dlq-ticket.")
            raise Exception("There is no current-dlq-ticket.")

    def add_comments_to_ticket(self, jira_connection, ticket, log_message):
        # parse log-message
        comment = jira_connection.add_comment(ticket, log_message)  # no Issue object required

    def get_current_dlq_ticket_status(self, jira_connection, current_dlq_ticket_key):
        current_dlq_ticket_status = jira_connection.issue(current_dlq_ticket_key).get_field("status")
        self.logger.debug(f"The current status of the dlq-ticket is {current_dlq_ticket_status}")
        return current_dlq_ticket_status

    def set_current_dlq_ticket_status(self, jira_connection, current_dlq_ticket_key, status):
        """
        status.name         | status.id
        Erfasst             | 121
        zurück zum Backlog  | 81
        In Arbeit           | 11
        zurück zu collected | 131
        Schließen           | 141
        """
        jira_connection.transition_issue(current_dlq_ticket_key, status)
        self.logger.debug(f"Set ticket {current_dlq_ticket_key} into new status {status}")

if __name__ == '__main__':
    jira = MyJira()
    client = jira.init_jira_connection()
    current_dlq_ticket_key = jira.get_current_dlq_ticket(client)
    print(f"current_dlq_ticket_key: {current_dlq_ticket_key}")
    current_dlq_ticket_status = jira.get_current_dlq_ticket_status(client, current_dlq_ticket_key)
    print(f"current_dlq_ticket_status: {current_dlq_ticket_status}")
    while jira.get_current_dlq_ticket_status(client, current_dlq_ticket_key).name == "Erfasst":
        print(current_dlq_ticket_status.name)
        jira.set_current_dlq_ticket_status(client, current_dlq_ticket_key, 11)
        # jira.add_comments_to_ticket(current_dlq_ticket_key)
        print(f"current_dlq_ticket_status: {current_dlq_ticket_status}")
