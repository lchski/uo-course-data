import requests

disciplines = ['HIS', 'POL', 'FLS']

for discipline in disciplines:
    page = requests.get('http://catalogue.uottawa.ca/en/courses/' + str.lower(discipline) + '/')

    file = open('pages/' + discipline + '.html', 'wb')
    file.write(page.content)
