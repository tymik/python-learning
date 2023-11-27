from weasyprint import HTML, CSS

string = '''<table>
    <thead>
        <tr>
            <th>Employee</th>
            <th>Working time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Doe</td>
            <td>8 hours and 30 minutes</td>
        </tr>
        <tr>
            <td>Jane Doe</td>
            <td>7 hours and 45 minutes</td>
        </tr>
    </tbody>
</table>'''

stylesheet = '''
    body {
        font-family: sans-serif;
    }
    thread tr {
        border-bottom: 3px solid black;
    }
    tbody td {
        border-bottom: 1px solid black;
    }
    thead th {
        font-weight: bold;
    }
    tbody tr td {
        padding-bottom: 5px;
    }
'''

html = HTML(string=string)
css = CSS(string=stylesheet)
html.write_pdf('report.pdf',stylesheets=[css])