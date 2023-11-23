#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Attendance module
@File        : attendance.csv.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:15
"""
import csv
import random


def attendanceMenu():
    """
    Construct the attendance.csv menu
    :return: None
    """
    menu_options = {
        '1': 'Mark attendance',
        '2': 'Update attendance',
        '3': 'Back'
    }

    print('\n')
    print('You have enter the attendance Menu')
    while True:
        print('\n')
        print('Please select an option:')
        for key, value in menu_options.items():
            print(f'{key}. {value}')

        option = input('Enter your option: ')
        if option == '1':
            markAttendance()
        elif option == '2':
            viewAttendance()
        elif option == '3':
            break
        else:
            print('Invalid option, please try again')


def markAttendance():
    """
    Mark attendance.csv
    :return: None
    """

    print('\n')
    print('Mark attendance')
    print('Instructions: Enter the activity name and the student name to mark attendance')

    activity_name = input('Enter activity name: ')
    if validateActivityName(activity_name):
        print('[WARN] Activity name already exist')
        markAttendance()
    token_activity = random.randint(1000000000, 9999999999)
    recordActivity(activity_name, token_activity)

    while True:
        name = input('Enter student\'s NRIC: ')
        if name == 'q':
            break
        elif name == 'd':
            print('Done marking attendance')
            break
        else:
            recordAttendance(activity_name, token_activity, name)
            print(f'{name} is marked as present. Enter \'d\' to done marking attendance.csv')


def validateActivityName(activity_name):
    """
    Validate activity name
    :param activity_name: activity name
    :return: True or False
    """

    with open('../data/activity.csv', 'r') as activity_file:
        for line in activity_file:
            if activity_name in line:
                return True
    return False


def recordActivity(activity_name, token_activity):
    """
    Record activity.csv helper function
    :param activity_name: activity
    :param token_activity: activity token
    :return: None
    """

    with open('../data/activity.csv', 'a') as activity_file:
        writer = csv.writer(activity_file)
        writer.writerow([activity_name, token_activity])


def recordAttendance(activity_name, token_activity, name):
    """
    Record attendance.csv helper function
    :param activity_name: activity
    :param token_activity: activity token
    :param name: student name
    :return: None
    """

    with open('../data/attendance.csv', 'a') as attendance_file:
        writer = csv.writer(attendance_file)
        writer.writerow([token_activity, name])
