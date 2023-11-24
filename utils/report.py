#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Report module
@File        : report.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:30
"""

import helper.percentage
import helper.output

def getActivitiesList() -> tuple:
    """
    Retrieve a list of activities.

    Returns:
    tuple: A tuple containing a list of activities (dict) and the total number of activities.
    """


    activity_list = []
    with open('./data/activity.csv', 'r') as file:
        counter = 0
        data = file.readlines()
        for line in data:
            if counter == 0:
                counter += 1
                continue

            line = line.replace('\n', '')
            activity_list.append({
                'activity_name': line.split(',')[0],
                'activity_token': line.split(',')[1],
            })
    return activity_list, len(activity_list)


def generateAnnualReport() -> dict:
    """
    Generate an annual report based on activity data.

    Returns:
    dict: A report containing various details for each activity.
    """


    report_list = []
    with open('./data/activity.csv', 'r') as file:
        counter = 0
        data = file.readlines()
        for line in data:
            if counter == 0:
                counter += 1
                continue

            line = line.replace('\n', '')

            report_list.append({
                'activity_name': line.split(',')[0],
                'present_count': line.split(',')[2],
                'absent_count': line.split(',')[3],
                'total_count': int(line.split(',')[2]) + int(line.split(',')[3]),
                'percentage': helper.percentage.calculate(
                    int(line.split(',')[2]),
                    int(line.split(',')[2]) + int(line.split(',')[3])
                )
            })
    return report_list


def generateIndividulAttendanceReport(NRIC: int) -> dict:
    """
    Generate an individual attendance report based on NRIC.

    Args:
    nric (int): The National Registration Identity Card number.

    Returns:
    dict: A report containing attendance details for the provided NRIC.
    """


    activity_list, total_activities = getActivitiesList()
    report = {'nric': NRIC,'total_activities': 0,'activities_attended': 0,'activities_missed': 0,'activities_list_attended': [],}
    final_report = []
    # get attended activities
    with open('./data/attendance.csv', 'r') as file:
        counter = 0
        data = file.readlines()
        for line in data:
            if counter == 0:
                counter += 1
                continue

            line = line.replace('\n', '')
            try:
                if line.split(',')[1] == str(NRIC):
                    report['activities_attended'] += 1
                    report['activities_list_attended'].append(line.split(',')[0])
            except IndexError:
                print('Invalid NRIC')
                return False, 'Invalid NRIC'
    report['total_activities'] = total_activities
    report['percentage'] = helper.percentage.calculate(
        report['activities_attended'],
        report['total_activities']
    )
    report['activities_missed'] = total_activities - report['activities_attended']

    for activity in activity_list:
        if activity['activity_token'] in report['activities_list_attended']:
            final_report.append({
                'activity_name': activity['activity_name'],
                'attended': True,
            })
        else:
            final_report.append({
                'activity_name': activity['activity_name'],
                'attended': False,
            })
    return report, final_report


def generate50PercAttendanceReport() -> dict:
    """
    Generate a report for activities with 50% or more attendance.

    Returns:
    dict: A report containing details of activities meeting the criteria.
    """


    report_list = []
    with open('./data/activity.csv', 'r') as file:
        counter = 0
        data = file.readlines()
        for line in data:
            if counter == 0:
                counter += 1
                continue

            line = line.replace('\n', '')
            if helper.percentage.calculate(
                    int(line.split(',')[2]),
                    int(line.split(',')[2]) + int(line.split(',')[3])
            ) >= 50:
                report_list.append({
                    'activity_name': line.split(',')[0],
                    'present_count': line.split(',')[2],
                    'absent_count': line.split(',')[3],
                    'total_count': int(line.split(',')[2]) + int(line.split(',')[3]),
                    'percentage': helper.percentage.calculate(
                        int(line.split(',')[2]),
                        int(line.split(',')[2]) + int(line.split(',')[3])
                    )
                })
    return report_list
def generateOverallAttendanceReport() -> str:
    """
    Generate an overall attendance report.

    Returns:
    str: A string representing the overall attendance report.
    """
    report_list = generateAnnualReport()

    if len(report_list) == 0:
        return 'No records found.'

    return f'Found {len(report_list)} records.\n' + helper.output.table(report_list)


def reportMenu():
    """
    Display the report menu and handle user choices.
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
            print(generateOverallAttendanceReport())

        elif option == '2':
            print('50% attendance report')
            report_list = generate50PercAttendanceReport()
            if len(report_list) == 0:
                print('No records found.')
                continue
            print(f'Found {len(report_list)} records.\n')
            print(helper.output.table(report_list))

        elif option == '3':
            while True:
                nric = input('Enter NRIC (0 to go back): ')
                if nric == '0':
                    break
                x, final_report = generateIndividulAttendanceReport(nric)
                if not x:
                    print('No records found.')
                    continue
                print(helper.output.table(final_report))
                print(f'Total activities: {x["total_activities"]}')
                print(f'Activities attended: {x["activities_attended"]}')
                print(f'Activities missed: {x["activities_missed"]}')
                print(f'Percentage: {x["percentage"]}%')
        elif option == '4':
            break
        else:
            print('Invalid option, please try again')