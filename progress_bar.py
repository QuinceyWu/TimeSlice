#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time ： 1/11/2024 1:53 PM
@Auth ： QuinceyWu
@File ：progress_bar.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import datetime


def calculate_progress(current_date):
    """计算年份进度"""
    start_of_year = datetime.date(current_date.year, 1, 1)
    end_of_year = datetime.date(current_date.year + 1, 1, 1)
    days_in_year = (end_of_year - start_of_year).days
    days_passed = (current_date - start_of_year).days
    progress_percentage = (days_passed / days_in_year) * 100
    return progress_percentage


def print_progress_bar(progress_percentage, bar_length=20):
    """打印进度条,长度设为20字符"""
    filled_length = int(bar_length * progress_percentage // 100)
    bar = '▓' * filled_length + '░' * (bar_length - filled_length)
    return bar


# 使用当天的日期作为输入
today = datetime.date.today()
progress_percentage = calculate_progress(today)
progress_bar = print_progress_bar(progress_percentage)

print(f"{progress_bar} {progress_percentage:.1f}%")
