from csv import DictReader
from datetime import datetime

employee_report = {}

with open('log.txt', 'r', encoding='utf8') as file:
    reader = DictReader(file)
    for row in reader:
        start_date = datetime.strptime(row['Start Date'],'%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(row['End Date'],'%Y-%m-%d %H:%M:%S')
        employee = row['Employee']
        customer = row['Client Name']
        duration = end_date - start_date

        if employee in employee_report:
            employee_report[employee] += duration
        else:
            employee_report[employee] = duration

print(employee_report)

for employee, duration in employee_report.items():
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, _ = divmod(remainder, 60)

    print(f'Working time: {employee} - {int(hours)} hours and {int(minutes)} minutes')