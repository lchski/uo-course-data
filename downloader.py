import requests

disciplines = ['HIS', 'POL']

for discipline in disciplines:
    page = requests.get('http://www.uottawa.ca/academic/info/regist/calendars/courses/' + discipline + '.html')

    file = open('pages/' + discipline + '.html', 'w')
    file.write(page.text)