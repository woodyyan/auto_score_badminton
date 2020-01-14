#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from tests.test_data.badminton_project_c001 import database, poster, param_helper, db_helper, constant
from tests.test_data.badminton_project_c001.constant import HOW_MUCH


def request_service(request_info: str) -> str:
    if request_info == HOW_MUCH:
        return poster.get_poster(database.load_workday_price_list(), database.load_weekend_price_list())
    else:
        act, name, day, start_time, end_time, number = param_helper.get_param_from_str(request_info)
        if param_helper.is_useful_act(act):
            if not param_helper.is_time_error(start_time, end_time):
                if db_helper.is_bookable(day, start_time, end_time, number):
                    return poster.get_success_result(number, day, start_time, end_time)

        return constant.SORRY
