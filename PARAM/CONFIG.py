class CONFIG:
    pass

class API_AUTH:

    API_KEY = "ZZ6CRqGZ"
    CLIENT_ID = "SAHW1028"
    EMAIL_ID = "shindenikhil102@gmail.com"
    PASSWORD = "Mastermind@123"
    MPIN = "2525"
    TOTP_SECURITY_KEY = "MALBI3B35CGKNABT6LJE62SKUY"

class URL:

    INSTRUMENT_LIST = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
    NSE_BANKNIFTY_URL = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
    NSE_BANKNIFTY_OPTION_CHAIN  = "https://www.nseindia.com/option-chain"


class HEADERS:

    NSEAPI = '''{'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                    'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                    'accept-encoding': 'gzip, deflate, br'}'''

class TOKEN_DF_FILTER:
    
    NAME = "BANKNIFTY"
    FUT_INTSTRUMENT = "FUTIDX"
    OPT_INTSTRUMENT = "OPTIDX"
    LOT_SIZE = "15"
    