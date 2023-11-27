from csv import DictReader
from datetime import datetime

from weasyprint import HTML

class PdfReport:
    def __init__(self):
        self.rows = []

    def add_row(self, employee: str, hours: int, minutes: int):
        self.rows.append(
            f'<tr><td>{employee}</td><td>{hours} hours and {minutes} minutes</td></tr>'
        )

    def save(self, filename: str):
        content = f'''<table>
                        <thead>
                            <tr>
                                <th>Employee</th>
                                <th>Working time</th>
                            </tr>
                        </thead>
                        <tbody>
                            {''.join(self.rows)}
                        </tbody>
                    </table>'''
        html = HTML(string=content)
        html.write_pdf(filename)

def read_file(filename: str):
    employee_report = {}

    with open(filename, 'r', encoding='utf8') as file:
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

    return employee_report

report = read_file('log.txt')

pdf_report = PdfReport()

for employee, duration in report.items():
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, _ = divmod(remainder, 60)

    print(f'Working time: {employee} - {int(hours)} hours and {int(minutes)} minutes')
    pdf_report.add_row(employee, hours, minutes)

pdf_report.save('employees_report.pdf')