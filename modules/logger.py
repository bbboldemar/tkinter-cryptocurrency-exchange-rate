
from datetime import datetime
import webbrowser
import logging

from constants import PATH_TO_DATAFILE, PATH_TO_LOGFILE


def logger_wr_info(message: str) -> None:
    logging.info(datetime.today().strftime('%D - %H:%M:%S ') + message)


def logger_wr_error(message: str) -> None:
    logging.error(datetime.today().strftime('%D - %H:%M:%S ') + message)


def DATAFILE_data_update(data_from_source: dict) -> None:
    data = data_from_source
    with open(PATH_TO_DATAFILE, 'a') as f:
        f.write(
            'at {} {} value is {}\n'.format(
                data['date_time'],
                data['currency_base'],
                data['cost']
            )
        )


def DATAFILE_open():
    webbrowser.open(PATH_TO_DATAFILE, new=1)


def LOGFILE_open():
    webbrowser.open(PATH_TO_LOGFILE, new=1)
