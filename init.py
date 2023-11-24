#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : init.py.py
@IDE         : PyCharm
@Date        : 24/11/2023 19:23
"""

""" You may run this file to initialize the project."""

import os

# initialize the data folder and data/activity.csv and data/attendance.csv

if not os.path.exists('data'):
    os.mkdir('data')
    print('data folder created')

if not os.path.exists('data/activity.csv'):
    with open('data/activity.csv', 'w') as f:
        f.write('activity_name, token_activity, present, absent\n')
    print('data/activity.csv created')

if not os.path.exists('data/attendance.csv'):
    with open('data/attendance.csv', 'w') as f:
        f.write('token_activity, name\n')
    print('data/attendance.csv created')

print('Initialization completed.')
