import requests
import bs4
import linked_list
import re

def get_courses():
    cs_directory = 'https://doc.sis.columbia.edu/sel/COMS_Fall2024_text.html'
    #curriculum = 'https://www.cs.columbia.edu/wp-content/uploads/2023/11/BS.pdf'

    # get the html of the CS directory
    try:
        cs_directory_response = requests.get(cs_directory)
        if cs_directory_response.status_code != 200:
            raise Exception
    except:
        print('Error: Could not connect to the CS directory')
        return None

    # extract the course information from the html
    cs_directory_soup = bs4.BeautifulSoup(cs_directory_response.text, 'html.parser')
    raw_courses = cs_directory_soup.find('pre').get_text()
    start = 0
    for i in range(4):
        start = raw_courses.find('\n', start) + 1
    raw_courses = raw_courses[start:]

    # create a linked list of courses
    courses = linked_list.SinglyLinkedList()
    course = raw_courses.split('\n', 1)[0] + '\n'
    raw_courses = raw_courses.split('\n', 1)[1]
    for line in raw_courses.split('\n'):
        if line.startswith(' '):
            course += line + '\n'
        else:
            parsed_course = {}
            course_lines = course.split('\n')
            first_line = course_lines[0].split()
            parsed_course['CourseCode'] = first_line[0] + first_line[1]
            parsed_course['SectionNumber'] = first_line[2]
            parsed_course['CallNumber'] = first_line[3]
            parsed_course['CreditCount'] = first_line[4]
            parsed_course['CourseTitle'] = course[31:65].strip()
            parsed_course['Time'] = course[65:100].strip()
            parsed_course['Instructor'] = course_lines[0][100:200].lstrip().strip()
            parsed_course['ClassType'] = course_lines[1].lstrip().strip()
            if len(course_lines) > 2:
                parsed_course['Note'] = course_lines[2].lstrip().strip()
            else:
                parsed_course['Note'] = None
            courses.add(parsed_course)
            course = line + '\n'

    return courses