import datetime
import logging

from pandas import DatetimeIndex

from properties import Props

import advertools as adv

import pandas as pd

logger = logging.getLogger(__name__)


class Logfile:

    def set_ticket_interval(self) -> tuple[DatetimeIndex]:
        ticket_interval_end = datetime.datetime.now()
        ticket_interval_start = ticket_interval_end - datetime.timedelta(hours=1)

        ticket_interval_end_final = ticket_interval_end.strftime('%Y-%m-%d %H')
        ticket_interval_start_final = ticket_interval_start.strftime('%Y-%m-%d %H')

        return ticket_interval_end_final, ticket_interval_start_final

    def analyze_logfile(self, interval_start, interval_end) -> dict:
        logger.debug("Start logfile analysis")

        props = Props()

        adv.logs_to_df(log_file=f"../{props.LOG_PATH}/{props.LOG_FILE}",

                       output_file=f"../{props.LOG_PATH}/{props.LOG_FILE}.parquet",

                       errors_file=f"../{props.LOG_PATH}/{props.LOG_FILE}.errors",

                       log_format=r'([\d]{4}-[\d]{2}-[\d]{2} \d\d:\d\d:\d\d,[\d]{3})'
                                  r'(.*)',

                       fields=['datetime', 'message'])

        df = pd.read_parquet(f"../{props.LOG_PATH}/{props.LOG_FILE}.parquet")

        df_today = df[df['datetime'].str.contains(f"{interval_start}|{interval_end}")]
        df_today_infolevel = df_today[df_today['message'].str.contains("INFO")]

        return df_today_infolevel.tail(100).to_string()


if __name__ == '__main__':
    lf = Logfile()
    interval_start, interval_end = lf.set_ticket_interval()
    dici = lf.analyze_logfile(interval_start, interval_end)
    print(dici)
