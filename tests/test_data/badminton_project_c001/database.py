#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime, date


class Rate:

    def __init__(self, time_range, fee):
        self.time_range = time_range
        self.fee = fee


def load_workday_price_list():
    workday_price_list = [Rate("9:00~12:00", 30),
                          Rate("12:00~18:00", 50),
                          Rate("18:00~20:00", 80),
                          Rate("20:00~22:00", 60)]
    return workday_price_list


def load_weekend_price_list():
    weekend_price_list = [Rate("9:00~12:00", 40),
                          Rate("12:00~18:00", 50),
                          Rate("18:00~22:00", 60)]
    return weekend_price_list


def get_datetime_now() -> datetime:
    return datetime.now()


def get_date_weekday(tmp_date: date):
    return tmp_date.weekday()
