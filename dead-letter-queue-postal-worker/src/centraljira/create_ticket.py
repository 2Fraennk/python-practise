from datetime import date
from properties import Props

import logging, sys

from jira import JIRA

logger = logging.getLogger(__name__)

jira = JIRA(server=Props.JIRA_URL,
            token_auth=Props().JIRA_LOGIN_TOKEN,
            )

date_today = date.today()
host = sys.argv[1]
service = sys.argv[2]
details = sys.argv[3]
labels = []
labels.append(sys.argv[4])

for arg in sys.argv:
    logger.debug(arg)

issue_dict = {
    'project': {'id': f"{Props.JIRA_PROJECT_ESB_ID}"},
    'summary': f"{date_today} - {service}",
    'description': f"Monitoring alert: {details}",
    'issuetype': {'name': 'ToDo'},
}

logger.info("START : Let me do the work for you...")

new_issue = jira.create_issue(fields=issue_dict)
logger.debug(f"Ticket {new_issue} created")

new_issue.update(assignee={'name': jira.current_user()})
logger.debug(f"Updated {new_issue}: assigned to  YOU")

new_issue.update(priority={"id": "1"})
logger.debug('Updated priority')

new_issue.update(fields={"labels": labels})
logger.debug('Set labels')

jira.transition_issue(new_issue, 121)
logger.debug(f"Ticket {new_issue.key} set to planing state")


logger.debug(f"END : Ticket {new_issue} update finished")
