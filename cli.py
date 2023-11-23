#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Main enterpoint for the application
@File        : cli.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:00
"""

import utils.attendance

def cliMenu():
    """
    Construct the CLI menu
    :return: None
    """
    menu_options = {
        '1': 'Report',
        '2': 'Attendance',
        '3': 'Exit'
    }
    print('Welcome to the Attendance System')
    for key, value in menu_options.items():
        print(f'{key}. {value}')


def constructCLI():
    """
    Construct the CLI
    :rtype: object
    :return: None
    """
    while True:
        cliMenu()
        option = input('Please select an option: ')
        if option == '1':
            print('Report')
        elif option == '2':
            utils.attendance.attendanceMenu()
        elif option == '3':
            break
        else:
            print('Invalid option, please try again')


if __name__ == '__main__':
    constructCLI()