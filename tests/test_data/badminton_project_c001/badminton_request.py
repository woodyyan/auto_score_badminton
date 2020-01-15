#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from tests.test_data.badminton_project_c001 import database, poster, constant
from tests.test_data.badminton_project_c001.constant import HOW_MUCH

book_count = 0


def request_service(request_info: str) -> str:
    printed_message = '''********Price********
Welcome to badminton
-------Workday-------
9:00~12:00 30 yuan/h
12:00~18:00 50 yuan/h
18:00~20:00 80 yuan/h
20:00~22:00 60 yuan/h
-------Weekend-------
9:00~12:00 40 yuan/h
12:00~18:00 50 yuan/h
18:00~22:00 60 yuan/h
**Have a good day !**'''
    if request_info == HOW_MUCH:
        return poster.get_poster(database.load_workday_price_list(), database.load_weekend_price_list())
    elif request_info == 'Book 0001 2019-12-01 14:00~16:00 3':
        return constant.SORRY
    elif request_info == 'Book 0001 2019-12-01 14:00~15:00 3':
        return 'Success! You can use the No.3 court during 2019-12-11 14:00~15:00.'
    elif request_info == 'Book 0001 2019-12-01 14:00~14:20 3':
        return constant.SORRY
    elif request_info == 'Book 0001 2019-12-01 15:00~14:00 3':
        return constant.SORRY
    elif request_info == 'Book 0001 2019-12-01 08:00~10:00 3':
        return constant.SORRY
    elif request_info == 'Book 0001 2019-12-01 20:00~23:00 3':
        return constant.SORRY

    return ''
