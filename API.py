import requests

from settings_checker import keys_read_API_key, keys_switch_API_key
from logger import logger_wr_error, logger_wr_info, DATAFILE_data_update
from main import API_URL

def load_data_from_API(currency:str, first_call_key:str, API_key:str) -> dict:
    """ Loads data for given cryptocurrency in JSON format from 
    "api.twelvedata.com" till any given keys are correct.
    Can get up to 24/2400 requests per minute/day.
    
    Args:
        - currency (str): given cryptocurrency symbol;
        - first_call_key (str): ;
        - API_key (str): reads API key from file.

    Returns:
        - dict: dictionary with "str" keys and values;
        - or None if:
            - all 3 keys are busted;
            - API returns errors 500, 414, 400, 404, 403.
    """
    logger_wr_info('Updating')
    response = requests.get(API_URL.format(currency, API_key))
    if response.json()['status'] == "ok":    
        logger_wr_info('Successful update')
        APIdata = {
            'currency_base': response.json()['meta']['currency_base'],
            'date_time': response.json()['values'][0]['datetime'],
            'cost': response.json()['values'][0]['close']
        }
        DATAFILE_data_update(APIdata)
        return APIdata
    else:
        logger_wr_error(response.json()['message'])
        if response.json()['code'] == 429 or 401:
            keys_switch_API_key()
        if keys_read_API_key() != first_call_key:
            logger_wr_info('Switching API key')
            return load_data_from_API(currency, first_call_key, keys_read_API_key())
        return None