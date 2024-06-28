from pykeepass import PyKeePass
import logging


class Props:
    stage = "Prod"

    # ACTIVEMQ CONFIG
    ACTIVEMQ_USER = ""
    ACTIVEMQ_PASSWORD_IN_CODE = ""   # set this var in case keepassxc below is NOT used

    # PLAYWRIGHT CONFIG
    HEADLESS = False
    LOG_FILE = "dead-letter-queue-postal-worker.log"
    LOG_PATH = "./logs"
    search_pattern_list = [r"^.*(HTTP-401).*(error message1).*$",
                           r"^.*(HTTP-401).*(error message2).*$",
                           r"^.*(HTTP-401).*(error message3).*$",
                           ]

    logger = logging.getLogger(__name__)
    filename = f"./../{LOG_PATH}/{LOG_FILE}"
    logging.basicConfig(level='DEBUG', filename=filename, filemode='a',
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    # JIRA CONFIG
    JIRA_KEEPASSXC_ITEM = "https://[FQDN]"
    JIRA_URL = JIRA_KEEPASSXC_ITEM
    JIRA_LOGIN_USER = ""
    JIRA_LOGIN_TOKEN_IN_CODE = ""   # set this var in case keepassxc below is NOT used
    JIRA_PROJECT_ESB_ID = ""

    # DOLOG CONFIG
    DOLOG_ACTIVATE_REMOTE_LOGGING = False
    DOLOG_HOST = "localhost"
    DOLOG_PORT = ""
    DOLOG_CA_CERT = ""
    DOLOG_LOGGING_TEAM = ""
    DOLOG_APPLICATION_NAME = "postal-worker"
    DOLOG_APPLICATION_STAGE = f"{stage}"

    # KEEPASSXC CONFIG
    KEEPASSXC_ACTIVATE_LOCAL_KEYSTORE = True
    KEEPASSXC_PWD = ""
    KEEPASSXC_DBPATH = ""

    # STAGE specific config
    title = f"Esb.Broker-1.{stage} : ActiveMQ Console"
    if stage == "Test":
        AMQ_KEEPASSXC_ITEM = "[URI]"
        JIRA_UPDATE_TICKET = False
        REMOVE_EMPTY_DLQS = True
    if stage == "Stage":
        AMQ_KEEPASSXC_ITEM = "[URI]"
        JIRA_UPDATE_TICKET = False
        REMOVE_EMPTY_DLQS = True
    if stage == "Prod":
        AMQ_KEEPASSXC_ITEM = "[URI]"
        JIRA_UPDATE_TICKET = True
        REMOVE_EMPTY_DLQS = True
    AMQ_URL = AMQ_KEEPASSXC_ITEM

    def keepassxc_connect(self):
        try:
            __kpc = PyKeePass(filename=self.KEEPASSXC_DBPATH, password=self.KEEPASSXC_PWD)
            return __kpc
        except Exception as e:
            logging.exception(f"Exception: {e}")
            raise Exception

    @property
    def JIRA_LOGIN_TOKEN(self):
        if self.KEEPASSXC_ACTIVATE_LOCAL_KEYSTORE:
            try:
                self.__JIRA_LOGIN_TOKEN = self.keepassxc_connect().find_entries(url=self.JIRA_KEEPASSXC_ITEM, first=True).password
            except Exception as e:
                logging.exception(f"Exception: {e}")
                raise Exception
        else:
            self.__JIRA_LOGIN_TOKEN = Props.JIRA_LOGIN_TOKEN_IN_CODE
        return self.__JIRA_LOGIN_TOKEN

    @JIRA_LOGIN_TOKEN.deleter
    def JIRA_LOGIN_TOKEN(self):
        del self.__JIRA_LOGIN_TOKEN

    @property
    def ACTIVEMQ_PASSWORD(self):
        if self.KEEPASSXC_ACTIVATE_LOCAL_KEYSTORE:
            try:
                self.__ACTIVEMQ_PASSWORD = self.keepassxc_connect().find_entries(url=self.AMQ_KEEPASSXC_ITEM, first=True).password
            except Exception as e:
                logging.exception(f"Exception: {e}")
                raise Exception
        else:
            self.__ACTIVEMQ_PASSWORD = Props.ACTIVEMQ_PASSWORD_IN_CODE
        return self.__ACTIVEMQ_PASSWORD



# see this example howto use the getters to get the secrets from keepass
if __name__ == '__main__':
    jira_login_token = Props().JIRA_LOGIN_TOKEN
    activemq_password = Props().ACTIVEMQ_PASSWORD
    print(jira_login_token)
    # del props.jira_login_token
    print(activemq_password)
    logging.debug("testlog")
