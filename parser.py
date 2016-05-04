import os
import json

from bs4 import BeautifulSoup

htmlFilesDir = "pages/"
htmlFiles = os.listdir(htmlFilesDir)

dataFilesDir = "data/"

files = []

courses = {}

for file in htmlFiles:
    if ".html" in file:
        files.append(htmlFilesDir + file)

for file in files:
    disciplineCourses = []

    courseCode = file.replace(htmlFilesDir, "").replace(".html", "")

    soup = BeautifulSoup(open(file, "r"), "html.parser")

    courseTables = soup.find_all(name="table", id="crsBox")

    for courseTable in courseTables:
        courseData = {}

        keysAndClasses = [
            ["code", "crsCode"],
            ["title", "crsTitle"],
            ["description", "crsDesc"],
            ["restriction", "crsRestrict"]
        ]

        for keyAndClass in keysAndClasses:
            dataElement = courseTable.find(class_=keyAndClass[1])

            if dataElement is not None:
                courseData[keyAndClass[0]] = dataElement.text
            else:
                courseData[keyAndClass[0]] = ""

        disciplineCourses.append(courseData.copy())

    courses[courseCode] = disciplineCourses

    with open(dataFilesDir + courseCode + ".json", "w", encoding="utf8") as jsonFile:
        json.dump(disciplineCourses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)

with open(dataFilesDir + "data.json", "w", encoding="utf8") as jsonFile:
    json.dump(courses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)
