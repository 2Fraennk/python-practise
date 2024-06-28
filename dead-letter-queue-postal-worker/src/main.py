import time, logging

from playwright.sync_api import Playwright, sync_playwright
from activemq.logfile import Logfile
from activemq.login import run_login
from activemq.queues import go2dead_letter_queue, find_existing_dead_letter_queues, go2queues
from activemq.dlq import run_retry_dl, get_messages_retry_locator_list_in_current_queue, remove_dlq
from properties import Props
from centraljira.my_jira import MyJira
from opensearch_logging.log_to_logstash import LogToLogstash

# TODO: try to place the following logstash_logger into the global vars section
# TODO: That leads to a refactoring of the current module to a class construct
if Props.DOLOG_ACTIVATE_REMOTE_LOGGING:
    logstash = LogToLogstash()
    logger = logstash.get_logger()
else:
    logger = logging.getLogger(__name__)


def run(playwright: Playwright) -> bool:
    if Props.DOLOG_ACTIVATE_REMOTE_LOGGING:
        logstash = LogToLogstash()
        logger = logstash.get_logger()
    else:
        logger = logging.getLogger(__name__)

    logger.debug("Start program: postal worker")

    """ Configure browser and run tests """
    logger.debug("Initialize browser")
    browser = playwright.firefox.launch(headless=bool(Props.HEADLESS))
    logger.debug("Initialize context")
    context = browser.new_context(
        http_credentials={
            "username": Props.ACTIVEMQ_USER,
            "password": Props().ACTIVEMQ_PASSWORD,
        }
    )

    page = context.new_page()

    try:
        # TODO: if necessary activate input to deliver dedicated message
        # dlq_name_input = run_input_dlq_name()
        # message_id = run_input_message_id()

        dlq_name_prefix = "DLQ."
        dlq_name = dlq_name_prefix
        message_id = "all"

        logger.debug(f"given parameters: {dlq_name}, {message_id}")

        run_login(page)
        page.on("dialog", lambda dialog: dialog.accept())

        if message_id == 'all':
            found_dead_letter_queues = find_existing_dead_letter_queues(page, dlq_name_prefix)
            if list(found_dead_letter_queues).__len__() > 0:
                for i in found_dead_letter_queues:
                    go2dead_letter_queue(page, i)
                    message_retry_locator_list = get_messages_retry_locator_list_in_current_queue(page, i)
                    if message_retry_locator_list.__len__() == 1:
                        if message_retry_locator_list.__contains__("This DLQ is empty and ready for being deleted!") and \
                                Props.REMOVE_EMPTY_DLQS:
                            logger.debug("Start removing DLQ")
                            go2queues(page)
                            remove_dlq(page, i)
                        else:
                            for locator in message_retry_locator_list:
                                logger.debug("Start message retry")
                                locator.click()
                                logger.info(f"Retry for message locator {locator} done")
                                time.sleep(1)
                    else:
                        if message_retry_locator_list.__len__() > 0:
                            for locator in message_retry_locator_list:
                                logger.debug("Start message retry")
                                locator.click()
                                logger.info(f"Retry for message locator {locator} done")
                                time.sleep(1)
                        else:
                            logger.info(f"Empty list or message is not ready for retry. Please investigate.")
                result = True
            else:
                logger.info("Could not find any DLQs")
                result = False
        elif message_id != "":
            logger.debug(f"message_id is set to: {message_id}")
            result_go2dead_letter_queue = go2dead_letter_queue(page, dlq_name)

            if result_go2dead_letter_queue:
                logger.debug(f"result_go2dead_letter_queue is set to: {result_go2dead_letter_queue}")
                result_run_retry_dl = run_retry_dl(page, dlq_name, message_id)
                logger.debug(f"result_run_retry_dl is set to: {result_run_retry_dl}")
                if result_run_retry_dl:
                    return True
                else:
                    return False
        else:
            logger.error("No message_id was given")
            result = False
    except Exception as e:
        logging.exception(f"Exception: {e}")
        raise Exception(f"Exception: {e}")
    finally:
        context.close()
        browser.close()


def run_input_dlq_name(dlq_name=None):
    dlq_name = input("please enter dlq_name: ")
    return dlq_name


def run_input_message_id(message_id=None):
    message_id = input("please enter message_id: ")
    return message_id


if Props.ACTIVEMQ_USER is None or Props().ACTIVEMQ_PASSWORD is None:
    logger.error("PLEASE SET *_USER AND *_PASSWORD VARIABLES")
    raise ValueError("PLEASE SET *_USER AND *_PASSWORD VARIABLES")

with sync_playwright() as playwright:
    run(playwright)
    # add jira client to add documentation of bot's run
    if Props.JIRA_UPDATE_TICKET:
        lf = Logfile()
        start, end = lf.set_ticket_interval()
        log_messages = lf.analyze_logfile(start, end)

        jira_client = MyJira()
        jira_connection = jira_client.init_jira_connection()
        current_dlq_ticket_key = jira_client.get_current_dlq_ticket(jira_connection)
        if jira_client.get_current_dlq_ticket_status(jira_connection, current_dlq_ticket_key).name == "Erfasst":
            jira_client.set_current_dlq_ticket_status(jira_connection, current_dlq_ticket_key, 11)
        jira_client.add_comments_to_ticket(jira_connection, current_dlq_ticket_key, log_messages)
        # while jira_client.get_current_dlq_ticket_status(current_dlq_ticket_key).name == "In Arbeit":
        #     jira_client.set_current_dlq_ticket_status(current_dlq_ticket_key, 141)
