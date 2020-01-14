#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from tests.test_data.badminton_project_c001 import constant


def get_poster(work_day_list: list, week_day_list: list) -> str:
    list_str = [constant.HEADER, constant.WELCOME, constant.WORKDAY] + [
        work_day_price.time_range + " " + str(work_day_price.fee) + constant.YUAN_PER_HOUR for work_day_price in
        work_day_list]
    list_str += [constant.WEEKEND, ] + [
        week_day_price.time_range + " " + str(week_day_price.fee) + constant.YUAN_PER_HOUR for week_day_price in
        week_day_list] + [constant.MESSAGE]
    poster = '\n'.join(list_str)
    return poster


def get_success_result(number: str, day: str, start_time: str, end_time: str) -> str:
    return 'Success! You can use the No.' + number + ' court during ' + day + ' ' + start_time + '~' + end_time + '.'
