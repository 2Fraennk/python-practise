from playwright.sync_api import Page
import time, logging, re
import activemq.queues
from properties import Props

logger = logging.getLogger(__name__)

now = time.time()

url = Props.AMQ_URL
stage = Props.stage
title = Props.title


def get_messages_retry_locator_list_in_current_queue(page: Page, dlq_name) -> list:
    logger.debug(f"Trying to find message_id for existing dead message")
    message_retry_locator_list = []
    table_locator = page.locator("//table[@id='messages']")
    table_locator.highlight()
    row_locator = table_locator.locator('tbody', has=page.locator('tr'))
    row_locator.highlight()
    time.sleep(1)
    row_locator_count = row_locator.count()
    if row_locator_count == 0:
        logger.debug(f"There are no messages. This DLQ is empty and ready for being deleted! counted: {row_locator_count}")
        message_retry_locator_list.append("This DLQ is empty and ready for being deleted!")
    if row_locator_count > 0:
        logger.debug(f"There are messages to be handled, counted: {row_locator_count}")
        message_links_in_row = row_locator.get_by_role('link')
        message_links_in_row.highlight()
        time.sleep(1)

        for locator in message_links_in_row.all():
            locator.highlight()
            time.sleep(1)
            result = locator.get_attribute('href')

            target2check = 'message.jsp'
            if str(result).__contains__(target2check):
                logger.info(f"Found message: {locator.all_text_contents()}")
                locator.click()
                row_locator_bci = page.locator('tr', has=page.locator('td'))
                row_locator_bci.highlight()
                time.sleep(1)
                target_td = row_locator_bci.get_by_text('Timestamp', exact=True)
                message_timestamp_locator = target_td.locator('//../td[2]')
                message_timestamp_locator_all_txt_content = message_timestamp_locator.all_text_contents()
                message_timestamp = str(message_timestamp_locator_all_txt_content).strip()
                logger.info(f"Found associated timestamp: {message_timestamp}")
                target_td = row_locator_bci.get_by_text('breadcrumbId', exact=True)
                message_breadcrumbid = target_td.locator('//../td[2]')
                logger.info(f"Found associated breadcrumbID: {message_breadcrumbid.all_text_contents()}")
                row_locator_cec = page.locator('tr', has=page.locator('td'))
                row_locator_cec.highlight()
                time.sleep(1)
                target_td = row_locator_cec.get_by_text('CamelExceptionCaught', exact=True)
                message_camel_exception_caught = target_td.locator('//../td[2]')
                logger.info(
                    f"Found associated camel_exception_caught: {message_camel_exception_caught.all_text_contents()}")
                retry_opportunity = analyze_message_retry_opportunity(message_camel_exception_caught.all_text_contents())
                activemq.queues.go2dead_letter_queue(page, dlq_name)

            target = 'moveMessage.action'
            if str(result).__contains__(target):
                if retry_opportunity:
                    logger.debug(f"Adding message locator to retry list")
                    message_retry_locator_list.append(locator)

    message_counter = table_locator.count()
    logger.debug(f"Message_id_locator_list: {message_retry_locator_list}")
    return message_retry_locator_list


def analyze_message_retry_opportunity(message_camel_exception_caught):
    logger.debug(f"message analysis for retry opportunity started.")
    retry_opportunity = False
    exception_input = str(message_camel_exception_caught[0])
    pattern_list = Props.search_pattern_list

    for p in pattern_list:
        pattern = re.compile(fr"{p}", re.DOTALL)
        if pattern.match(exception_input):
            retry_opportunity = True
            logger.debug(f"Let's retry processing the current message.")
    logger.debug(f"Message analysis finished.")
    return retry_opportunity


def find_message_in_current_queue(page: Page, dlq_name, message_id) -> bool:
    logger.debug(f"Trying to find message_id {message_id}")
    table_locator = page.locator("//table[@id='messages']")
    table_locator.highlight()
    row_locator = table_locator.locator('tr', has=page.locator('td', has_text=message_id))
    row_locator.highlight()
    row_locator_count = row_locator.count()
    logger.debug(f"Messages to be deleted counter: {row_locator_count}")

    # returned object must be unique to avoid multiple selections e.g. in case of a cropped message_id being found multiple times
    if row_locator_count == 1:
        result = True
    else:
        result = False
    return result


def run_retry_dl(page: Page, dlq_name, message_id) -> bool:
    logger.info("Retry the dead letter processing")
    result_find_message_in_current_queue = find_message_in_current_queue(page, dlq_name, message_id)

    # active handling popup dialogs by playwright
    page.once("dialog", lambda dialog: dialog.accept())

    # returned object must be unique to avoid multiple selections e.g. in case of a cropped message_id being found multiple times
    if result_find_message_in_current_queue:
        table_locator = page.locator("//table[@id='messages']")
        logger.debug(f"Found messages inside DLQ: {dlq_name}")
        row_locator = table_locator.locator('tr', has=page.locator('td', has_text=message_id))
        logger.debug(f"Found message: {message_id}")
        link_locator = row_locator.locator('//../td[9]/a[2]')
        if link_locator.count() == 1:
            logger.debug(f"Ensured message found is unique: {message_id}")
            link_locator.click()

            # check if message is gone after retry
            result_find_message_in_current_queue = find_message_in_current_queue(page, dlq_name, message_id)

            assert result_find_message_in_current_queue is False  # assert message has been deleted
            logger.info(f"Message {message_id} from queue {dlq_name} has been deleted")
            result = True
        else:
            logger.error("retry-link could not be found or is more than exactly 1")
            raise ValueError("retry-link could not be found or is more than exactly 1")
            result = False
    else:
        logger.debug("message_id could not be found or is more than exactly 1")
        result = False

    return result


def remove_dlq(page: Page, dlq_name) -> bool:
    logger.info(f"Remove DLQ {dlq_name}")

    queue2remove = page.get_by_role("link", name=dlq_name, exact=True)
    queue2remove.highlight()
    time.sleep(1)

    table_locator = page.locator("//table[@id='queues']")
    row_locator = table_locator.locator('tr', has=page.locator('td', has_text=dlq_name))
    row_locator.highlight()
    logger.debug(f"Found DLQ: {dlq_name}")
    link_locator = row_locator.locator('//../td[7]/a[3]')
    link_locator.highlight()
    if link_locator.count() == 1:
        logger.debug(f"Ensured DLQ found is unique: {dlq_name}")
        link_locator.click()
        result = True
    else:
        result = False

    return result
