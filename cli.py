#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Main enterpoint for the application
@File        : cli.py
@IDE         : PyCharm
@Date        : 23/11/2023 22:00
"""
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
            reportMenu()
        elif option == '2':
            attendanceMenu()
        elif option == '3':
            break
        else:
            print('Invalid option, please try again')


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
                'percentage': calculate(
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
    report['percentage'] = calculate(
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
            if calculate(
                    int(line.split(',')[2]),
                    int(line.split(',')[2]) + int(line.split(',')[3])
            ) >= 50:
                report_list.append({
                    'activity_name': line.split(',')[0],
                    'present_count': line.split(',')[2],
                    'absent_count': line.split(',')[3],
                    'total_count': int(line.split(',')[2]) + int(line.split(',')[3]),
                    'percentage': calculate(
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

    return f'Found {len(report_list)} records.\n' + table(report_list)


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
            print(table(report_list))

        elif option == '3':
            while True:
                nric = input('Enter NRIC (0 to go back): ')
                if nric == '0':
                    break
                x, final_report = generateIndividulAttendanceReport(nric)
                if not x:
                    print('No records found.')
                    continue
                print(table(final_report))
                print(f'Total activities: {x["total_activities"]}')
                print(f'Activities attended: {x["activities_attended"]}')
                print(f'Activities missed: {x["activities_missed"]}')
                print(f'Percentage: {x["percentage"]}%')
        elif option == '4':
            break
        else:
            print('Invalid option, please try again')

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

    token_activity = randint(1000000000, 9999999999)
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

def table(data: dict, width: int = 20) -> str:
    """
    Returns activity summary in a formatted table with dynamic headers.

    Args:
    - data (list): A list of dictionaries containing activity-related data.
                   Each dictionary should contain keys corresponding to the table headers.
    - width (int): The width of each column in the table.

    Returns:
    Returns the activity summary in the specified format as a string.
    """

    return_string = ""
    header_format = ""

    headers = list(data[0].keys())

    for header in headers:
        header_format += "{:<" + str(width) + "s} | "  # Adjust the width as needed

    return_string += "=" * (int(width) * len(headers) + 3 * (len(headers) - 1)) + "\n"
    for header in headers:
        if header == headers[-1]:
            return_string += "{:<{}}\n".format(header, width)
        else:
            return_string += "{:<{}} | ".format(header, width)

    return_string += "=" * (int(width) * len(headers) + 3 * (len(headers) - 1)) + "\n"

    for activity in data:
        for key in headers:
            if key == headers[-1]:
                return_string += "{:<{}}".format(str(activity[key]), width)
            else:
                return_string += "{:<{}} | ".format(str(activity[key]), width)
        return_string += "\n"

    return return_string

def calculate(presnt: int, total: int,toFixed: int = 2) -> float:
    """
    Calculate percentage.

    Args:
    present (float): The number of present items.
    total (float): The total number of items.
    to_fixed (int, optional): Number of decimal places in the result. Default is 2.

    Returns:
    float: The calculated percentage.
    """
    try:
        return round((presnt / total) * 100, toFixed)
    except ZeroDivisionError:
        return 0.00

def randint(a: int, b:int) -> int:
    """
    Return random integer in range [a, b], including both end point.
    """
    import random
    return random.randint(a, b)


if __name__ == '__main__':
    constructCLI()