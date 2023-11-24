#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Attendance module
@File        : attendance.csv.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:15
"""

import random

def attendanceMenu():
    """
    Display the attendance menu and handle user choices.
    """


    menu_options = {
        '1': 'Mark attendance',
        '2': 'Back'
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
            break
        else:
            print('Invalid option, please try again')


def markAttendance():
    """
    Mark attendance for an activity.
    """

    print('\n')
    print('Mark attendance')
    print('Instructions: Enter the activity name and the student name to mark attendance')

    activity_name = input('Enter activity name: ')

    if validateActivityName(activity_name):
        print('[WARN] Activity name already exist')
        markAttendance()

    total_student = input('Enter total student: ')

    token_activity = random.randint(1000000000, 9999999999)
    counter = 0

    while True:
        name = input('Enter student\'s NRIC: ')
        if name == 'q':
            break
        elif name == 'd':
            print('Done marking attendance')

            absent_student = int(total_student) - counter
            present_percentage = round((counter / int(total_student)) * 100, 2)

            print(f'Total student: {total_student}')
            print(f'Present student: {counter}')
            print(f'Absent student: {absent_student}')
            print(f'Present percentage: {present_percentage}%')

            recordActivity(activity_name, token_activity, counter, absent_student)
            break
        else:
            recordAttendance(activity_name, token_activity, name)
            print(f'{name} is marked as present. Enter \'d\' to done marking attendance')
            counter += 1


def validateActivityName(activity_name: str) -> bool:
    """
    Validate activity name.

    Args:
    activity_name (str): The name of the activity to validate.

    Returns:
    bool: True if the activity name exists, False otherwise.
    """

    with open('./data/activity.csv', 'r') as activity_file:
        for line in activity_file:
            if activity_name in line:
                return True
    return False


def recordActivity(activity_name: str, token_activity: int, present_student: int, absent_student: int) -> None:
    """
    Record activity.csv helper function.

    Args:
    activity_name (str): Name of the activity.
    token_activity (int): Activity token.
    present_student (int): Number of present students.
    absent_student (int): Number of absent students.
    """

    with open('./data/activity.csv', 'a') as activity_file:
        activity_file.write(f'{activity_name},{token_activity},{present_student},{absent_student}\n')


def recordAttendance(activity_name: str, token_activity: int, name: str) -> None:
    """
    Record attendance.csv helper function.

    Args:
    activity_name (str): Name of the activity.
    token_activity (int): Activity token.
    name (str): Name of the student.
    """

    with open('./data/attendance.csv', 'a') as attendance_file:
        attendance_file.write(f'{token_activity},{name}\n')
