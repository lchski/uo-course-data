import os
import json
import re

from bs4 import BeautifulSoup

htmlFilesDir = "pages/"
htmlFiles = os.listdir(htmlFilesDir)

dataFilesDir = "data/"

files = []

courses = []

disciplines = []


class UoCourseListParser:
    def __init__(self, disciplineFile):
        self.soup = BeautifulSoup(open(disciplineFile, "r", encoding="utf-8"), "html.parser")

        self.courses = []

        self.start_process()

    def start_process(self):
        courseBlocks = self.soup.find_all(name="div", class_="courseblock")

        for courseBlock in courseBlocks:
            courseData = UoCourseSingleParser(courseBlock)

            self.courses.append({
                'code': courseData.code,
                'credits': courseData.credits,
                'year': courseData.year,
                'language': courseData.language,
                'title': courseData.title,
                'description': courseData.description,
                'extraDetails': courseData.extra_details
            })


class UoCourseSingleParser:
    def __init__(self, courseBlock):
        self.code = None
        self.credits = None
        self.year = None
        self.language = None
        self.title = None
        self.description = None
        self.extra_details = None

        self.extract_data(courseBlock)

    def extract_data(self, courseBlock):
        titleCodeCreditsElement = courseBlock.find(class_="courseblocktitle")

        titleCredits = re.match(r"([a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ/ ]*)\(([0-9])", titleCodeCreditsElement.text[9:])

        self.code = titleCodeCreditsElement.text[0:8].replace(u'\xa0', ' ')
        self.credits = int(titleCredits.group(2)) if titleCredits is not None else ''
        self.year = self.extract_year_from_code(self.code)
        self.language = self.extract_language_from_code(self.code)
        self.title = titleCredits.group(1).strip() if titleCredits is not None else ''
        self.description = self.extract_description(courseBlock)
        self.extra_details = self.extract_extra_details(courseBlock)

    def extract_year_from_code(self, code):
        return int(code[4])

    def extract_language_from_code(self, code):
        return "English" if 1 <= int(code[5]) <= 4 else "French" if 5 <= int(code[5]) <= 8 else "Bilingual/Unofficial/Unspecified"

    def extract_description(self, courseBlock):
        descriptionElement = courseBlock.find(class_="courseblockdesc")

        if descriptionElement is not None:
            return descriptionElement.text.replace('\n', '').strip()
        else:
            return ''

    def extract_extra_details(self, courseBlock):
        details = []
        detailElements = courseBlock.find_all(class_="courseblockextra")

        for detail in detailElements:
            details.append(detail.text)

        return details


for file in htmlFiles:
    if ".html" in file:
        files.append(htmlFilesDir + file)

for file in files:
    disciplineCode = file.replace(htmlFilesDir, "").replace(".html", "")

    disciplineData = UoCourseListParser(file)

    print(disciplineData.courses[0])

    courses.extend(disciplineData.courses.copy())

    disciplines.append(disciplineCode)

#     with open(dataFilesDir + disciplineCode + ".json", "w", encoding="utf8") as jsonFile:
#         json.dump(disciplineCourses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)
#
# with open(dataFilesDir + "data.json", "w", encoding="utf8") as jsonFile:
#     json.dump(courses, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)
#
# with open(dataFilesDir + "disciplines.json", "w", encoding="utf8") as jsonFile:
#     json.dump(disciplines, jsonFile, sort_keys=True, indent=4, ensure_ascii=False)
