import logging
import logstash

from properties import Props


class LogToLogstash:
    """
    This class lets you log your messages to a central logstash endpoint.

    """


    host = Props.DOLOG_HOST

    logstash_logger = logging.getLogger('python-logstash-logger')
    logstash_logger.setLevel(logging.DEBUG)
    handler = logstash.HTTPLogstashHandler(Props.DOLOG_HOST, Props.DOLOG_PORT, ssl=False, verify=False)
    logstash_logger.addHandler(handler)

    def get_logger(self):
        """
        Return a logger for logging to a central logstash endpoint.

        """
        return self.logstash_logger

    def info(self, message: str):
        """
        Set Loglevel to INFO and log the given message with the specific logstash_logger.

        """
        test_logger = self.test_logger
        test_logger.info(f"This is a test message: {message}")

    def debug(self, message: str):
        """
        Set Loglevel to DEBUG and log the given message with the specific logstash_logger.

        """
        test_logger = self.test_logger
        test_logger.debug(f"This is a debug message: {message}")

    def error(self, message: str):
        """
        Set Loglevel to ERROR and log the given message with the specific logstash_logger.

        """
        test_logger = self.test_logger
        test_logger.error(f"This is an error message: {message}")

    def exception(self, message: str):
        """
        Set Loglevel to EXCEPTION and log the given message with the specific logstash_logger.

        """
        test_logger = self.test_logger
        test_logger.exception(f"This is an exception message: {message}")

    # test_logger.error('test logstashpy error message.')
    #
    # test_logger.warning('test logstashpy warning message.')
    #
    # # add extra field to logstash message
    # extra = {
    #     'logging_team': Props.DOLOG_LOGGING_TEAM,
    #     'logging_application_name': Props.DOLOG_APPLICATION_NAME,
    #     'logging_application_stage': Props.DOLOG_APPLICATION_STAGE,
    #     'test_string': 'cool!',
    #     'test_boolean': True,
    #     'test_dict': {'a': 1, 'b': 'c'},
    #     'test_float': 1.23,
    #     'test_integer': 123,
    #     'test_list': [1, 2, '3'],
    # }
    #
    # test_logger.info('test extra fields', extra=extra)


if __name__ == '__main__':
    logstash = LogToLogstash()
    logstash_logger = logstash.get_logger()
    logstash_logger.info("testesttest")
