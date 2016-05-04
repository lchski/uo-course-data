import os
from bs4 import BeautifulSoup

htmlFilesDir = 'pages/'
htmlFiles = os.listdir(htmlFilesDir)

files = []

for file in htmlFiles:
    if '.html' in file:
        files.append(htmlFilesDir + file)

for file in files:
    soup = BeautifulSoup(open(file, 'r'), 'html.parser')

    print(soup.table)