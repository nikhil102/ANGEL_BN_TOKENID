# Libraries
import requests
import json
import pandas as pd
from datetime import date
import ast
from   PARAM.CONFIG import URL as CONFIG_URL
from   PARAM.CONFIG import HEADERS  as HEADERS



url_bnf = CONFIG_URL.NSE_BANKNIFTY_URL
url_oc = CONFIG_URL.NSE_BANKNIFTY_OPTION_CHAIN
header_string = CONFIG_URL.NSE_BANKNIFTY_OPTION_CHAIN
header_string = HEADERS.NSEAPI

STRIKE_PRICE_BASE = CE_STRIKE_PRICE = PE_STRIKE_PRICE = 0
CE_STRIKE_PRICE_UPPER_RANGE_VAL = 0
CE_STRIKE_PRICE_LOWER_RANGE_VAL = 0
PE_STRIKE_PRICE_UPPER_RANGE_VAL = 0
PE_STRIKE_PRICE_LOWER_RANGE_VAL = 0

# Headers
headers = ast.literal_eval(header_string)

sess = requests.Session()
cookies = dict()

def set_cookie():
    request = sess.get(url_oc, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    
def get_data():
    set_cookie()
    response = sess.get(url_bnf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==401):
        set_cookie()
        response = sess.get(url_bnf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==200):
        return response.text
    return ""

def get_filter_data():
    res = get_data()
    if res == None or res == "":
       return {}
    else: 

        json_object = json.loads(res)        
        if bool(json_object):
            
           records = {}
           filtered = {}
           expiryDates= {}
           index= {}
           Last_price= 0
           expiryDates = []
           
           if 'records' in json_object:
               records = json_object['records']
           else:
               return {}
           
           if 'filtered' in json_object:
               filtered = json_object['filtered']
           else:
               return {}
           
           if 'expiryDates' in records:
               expiryDates = records['expiryDates']
           else:
               return {} 
           
           if 'index' in records:
               index = records['index']
           else:
               return {}
           
           if 'last' in index:
               Last_price = index['last']
           else:
               return {}
           
        if len(expiryDates) > 0:
            EX_ROW_DF = pd.DataFrame(expiryDates,columns = ['expiryDates'])
            EX_ROW_DF['expiryDates'] = pd.to_datetime(EX_ROW_DF['expiryDates'])
            today = date.today()
            TODAYDATE_CHECK= today.strftime('%Y-%b-%d')
            EX_DF = pd.DataFrame(EX_ROW_DF[(EX_ROW_DF['expiryDates']> TODAYDATE_CHECK)])
            EX_DF['expiryDates'] = EX_DF['expiryDates'].dt.strftime('%d%b%Y')
            EX_DF.reset_index(drop=True ,inplace = True)
            if not EX_DF.empty:
                current_expiry_date = EX_DF.expiryDates.iloc[0]  
        else:
            return {} 
            

        if current_expiry_date != "":
            EXPIRYDATA = str(current_expiry_date).upper()
            
        if int(Last_price) > 0:
            
            Last_price = int(Last_price)
            STRIKE_PRICE_BASE = Last_price / 100
            STRIKE_PRICE_BASE = int(STRIKE_PRICE_BASE)
            CE_STRIKE_PRICE = STRIKE_PRICE_BASE * 100
            PE_STRIKE_PRICE = CE_STRIKE_PRICE + 100 
            CE_STRIKE_PRICE_UPPER_RANGE_VAL = CE_STRIKE_PRICE + 1000
            CE_STRIKE_PRICE_LOWER_RANGE_VAL = CE_STRIKE_PRICE - 1000
            PE_STRIKE_PRICE_UPPER_RANGE_VAL = PE_STRIKE_PRICE + 1000
            PE_STRIKE_PRICE_LOWER_RANGE_VAL = PE_STRIKE_PRICE - 1000
            
            new_entry = {
                
                     'CURRENT_EXPIRY_DATE': current_expiry_date,
                     'EXPIRYDATA':EXPIRYDATA,
                     'LAST_PRICE': Last_price,
                     'CURRENT_PRICE': Last_price,
                     'CE_STRIKE_PRICE':CE_STRIKE_PRICE,
                     'PE_STRIKE_PRICE':PE_STRIKE_PRICE,
                     'CE_SP_UP_R_VALUE':CE_STRIKE_PRICE_UPPER_RANGE_VAL,
                     'CE_SP_LOW_R_VALUE':CE_STRIKE_PRICE_LOWER_RANGE_VAL,
                     'PE_SP_UP_R_VALUE':PE_STRIKE_PRICE_UPPER_RANGE_VAL,
                     'PE_SP_LOW_R_VALUE':PE_STRIKE_PRICE_LOWER_RANGE_VAL,
                     
                    }
        
        return new_entry

# database.insert("option_day_data", new_entry)
