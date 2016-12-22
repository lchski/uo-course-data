import requests

disciplines = ['HIS', 'POL', 'PHI', 'ENG', 'LIN', 'FEM', 'FLS']

for discipline in disciplines:
    page = requests.get('http://www.uottawa.ca/academic/info/regist/calendars/courses/' + discipline + '.html')

    file = open('pages/' + discipline + '.html', 'wb')
    file.write(page.content)
