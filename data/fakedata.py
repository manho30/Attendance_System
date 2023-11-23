from faker import Faker
import csv
import random

# Initializing Faker to generate fake data
fake = Faker()

# Generating a list of activities with tokens and names
activities = [{'act_name': f"Activity_{i}", 'token': fake.uuid4()} for i in range(1, 11)]  # 10 activities

# Generating a list of people with names and tokens
people = [{'name': fake.name(), 'token': fake.uuid4()} for _ in range(200)]

# Dictionary to track which activities each person participates in
participation = {person['token']: random.sample(activities, random.randint(1, 5)) for person in people}

# Writing activity data to activity.csv
with open('activity.csv', 'w', newline='') as activity_file:
    activity_writer = csv.writer(activity_file)
    activity_writer.writerow(['token', 'act_name'])

    for activity in activities:
        activity_writer.writerow([activity['token'], activity['act_name']])

# Writing attendance data to attendance.csv
with open('attendance.csv', 'w', newline='') as attendance_file:
    attendance_writer = csv.writer(attendance_file)
    attendance_writer.writerow(['name', 'token', 'activity'])

    # Assigning people to activities
    for person in people:
        for activity in participation[person['token']]:
            attendance_writer.writerow([person['name'],activity['token']])

print("Data generation completed!")
