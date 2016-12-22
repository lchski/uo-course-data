import os
import json

from bs4 import BeautifulSoup

htmlFilesDir = "pages/"
htmlFiles = os.listdir(htmlFilesDir)

dataFilesDir = "data/"

files = []

courses = []

disciplines = []

for file in htmlFiles:
    if ".html" in file:
        files.append(htmlFilesDir + file)

for file in files:
    disciplineCourses = []

    disciplineCode = file.replace(htmlFilesDir, "").replace(".html", "")

    soup = BeautifulSoup(open(file, "r", encoding="utf-8"), "html.parser")

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

        courseData["year"] = courseData["code"][3]
        courseData["language"] = "English" if 1 <= int(courseData["code"][4]) <= 4 else "French" if 5 <= int(courseData["code"][4]) <= 8 else "Bilingual/Unofficial/Unspecified"

        disciplineCourses.append(courseData.copy())

    courses.extend(disciplineCourses.copy())

    disciplines.append(disciplineCode)

    with open(dataFilesDir + disciplineCode + ".json", "w", encoding="utf8") as jsonFile:
        json.dump(disciplineCourses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)

with open(dataFilesDir + "data.json", "w", encoding="utf8") as jsonFile:
    json.dump(courses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)

with open(dataFilesDir + "disciplines.json", "w", encoding="utf8") as jsonFile:
    json.dump(disciplines, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)
