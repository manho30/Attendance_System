#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Report module
@File        : report.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:30
"""

def reportMenu():
    """
    Construct the report menu
    :return: None
    """
    menu_options = {
        '1': 'Overall attendance report',
        '2': '50% attendance report',
        '3': 'Individual attendance report',
        '4': 'Back'
    }

    print('\n')
    print('You have enter the report Menu')
    while True:
        print('\n')
        print('Please select an option:')
        for key, value in menu_options.items():
            print(f'{key}. {value}')

        option = input('Enter your option: ')
        if option == '1':
            print('Overall attendance report')
        elif option == '2':
            print('50% attendance report')
        elif option == '3':
            print('Individual attendance report')
        elif option == '4':
            break
        else:
            print('Invalid option, please try again')
