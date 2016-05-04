import os
import json

from bs4 import BeautifulSoup

htmlFilesDir = "pages/"
htmlFiles = os.listdir(htmlFilesDir)

files = []

courses = []

for file in htmlFiles:
    if ".html" in file:
        files.append(htmlFilesDir + file)

for file in files:
    disciplineCourses = []

    soup = BeautifulSoup(open(file, "r"), "html.parser")

    courseTables = soup.find_all(name="table", id="crsBox")

    for courseTable in courseTables:
        courseData = {}

        keysAndClasses = [
            ["code", "crsCode"],
            ["title", "crsTitle"],
            ["description", "crsDesc"]
        ]

        for keyAndClass in keysAndClasses:
            courseData[keyAndClass[0]] = courseTable.find(class_=keyAndClass[1]).text

        disciplineCourses.append(courseData.copy())

    courses.append(disciplineCourses)

print(json.dumps(courses, sort_keys=True, indent=4))