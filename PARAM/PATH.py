import os
from datetime import date

def TODAYDATE_IN_TOKEN_FORMAT_STR_UPPER():
    today = date.today()
    TODAYDATE_IN_TOKEN_FORMAT = today.strftime('%d%b%Y')
    return str(TODAYDATE_IN_TOKEN_FORMAT).upper()


CURRENT_PATH = os.getcwd()

TODAYDATE_IN_TOKEN_FORMAT_STR_UPPER = TODAYDATE_IN_TOKEN_FORMAT_STR_UPPER()
CURRENT_JSON_RES_BANKNIFTY_PATH = os.path.join(CURRENT_PATH, 'DATA','ANGEL_BANKNIFTY_TOKENID')
SPL_DAY_PATH = os.path.join(CURRENT_PATH, 'DATA','SPL_DAY')
FILE_NAME_TOKEN_LIST = TODAYDATE_IN_TOKEN_FORMAT_STR_UPPER +'.csv'
JSON_FILE_NAME_TOKEN_LIST = TODAYDATE_IN_TOKEN_FORMAT_STR_UPPER +'.json'
SPL_DAY_FILE_NAME = 'LIST.csv'
CURRENT_JSON_RES_BANKNIFTY_FILEPATH = os.path.join(CURRENT_JSON_RES_BANKNIFTY_PATH,JSON_FILE_NAME_TOKEN_LIST)
SPL_DAY_FILE_PATH = os.path.join(SPL_DAY_PATH,SPL_DAY_FILE_NAME)

