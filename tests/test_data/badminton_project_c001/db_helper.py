#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# from unit.db import DATABASE
from tests.test_data.badminton_project_c001 import param_helper, DATABASE


def is_bookable(day: str, start_time: str, end_time: str, number: str) -> bool:
    key = day + '-' + number
    start_hour, = param_helper.time_to_number(start_time)
    end_hour, = param_helper.time_to_number(end_time)
    times = [num for num in range(start_hour, end_hour)]

    if key in DATABASE.keys():
        hour_list = DATABASE.get(key)
        if not set(hour_list).intersection(set(times)):
            DATABASE.update(key, hour_list + range)
    else:
        DATABASE.setdefault({key: times})
        return True

    return False
