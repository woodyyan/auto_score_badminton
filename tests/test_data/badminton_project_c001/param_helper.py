#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from tests.test_data.badminton_project_c001 import constant


def get_param_from_str(request_info: str) -> [str, str, str, str, str, str]:
    act, name, day, time, number = request_info.split(' ')
    start_time, end_time = time.split('~')
    return act, name, day, start_time, end_time, number


def is_useful_act(act: str) -> bool:
    if act == constant.BOOK or act == constant.CANCEL:
        return True
    else:
        return False


def is_time_error(start_str: str, end_str: str) -> bool:
    start_hour, start_minutes = time_to_number(start_str)
    end_hour, end_minutes = time_to_number(end_str)

    if start_minutes != 0 or end_minutes != 0:
        return False

    if end_hour >= start_hour:
        return False

    if start_hour < 9 or end_hour > 22:
        return False
    return True


def time_to_number(time_str:str) ->[int, int]:
    hour, minutes = time_str.split(':')
    return int(hour), int(minutes)
