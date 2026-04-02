# This is the functions file, It is imported to the main file,Supporting the readability of the main file by seperating all the funcitions

import time
import json
import sys

def save(students):
    with open('data.json', 'w') as f:
        json.dump(students, f, indent=4)

def return_int(english_grade, math_grade, science_grade, birth_year):
    if all(isinstance(x, str) and x.isdigit() for x in (english_grade, math_grade, science_grade, birth_year)):
        return int(english_grade), int(math_grade), int(science_grade), int(birth_year)

    else:
        return '♦ All the grades and the birth year should be numbers', '', '', ''
        
def check_data(students, name, english_grade, math_grade, science_grade, birth_year):
    if any(isinstance(x, str) and not x.isdigit() for x in (english_grade, math_grade, science_grade,)):
        return '♦ All the grades should be a number'
    
    elif any(x > 100 for x in (english_grade, math_grade, science_grade)):
        return '♦ Grades of math and english and science should all be between 0-100!'

    elif not isinstance(name, str):
        return '♦ The name should be string!'

    elif ' ' in name or name == '':
        return '♦ The name should not contain spaces or be empty!'

    elif name.isdigit():
        return '♦ The name should be a string!'
    elif len(name) > 12:
        return  '♦ The student name is too long!'

    elif len(name) < 2:
        return '♦ The student name is too short!'

    elif name in students.keys():
        return '♦ The student name already exists!'
    
    elif not birth_year in range(2000, 2020):          # predicted age of a student in 2026: (2000/2019)
        return '♦ Enter a valid student birth year 2000/2019!'    
        
    else:
        return 'valid data'

    
def new_student(students, name, english_grade, math_grade, science_grade, percentage, birth_year):
        students[name] = {
            'grades':[english_grade, math_grade, science_grade],
            'percentage' : percentage,
            'birth_year' : birth_year,
            }
        return students

def calc_percentage(english_grade, math_grade, science_grade):
    percentage = round(((english_grade + math_grade + science_grade)/300)*100, 2)
    return percentage

def remove_student(students, name):
    del students[name]
    save(students)

def show_student(students, name_search, percentage, birth_year):
    grades = students[name_search]['grades']
    student = [grades[0], grades[1], grades[2], percentage, birth_year]
    return student

def rank(students):
    all_percentages = []
    all_names = []
    for student in students.values():
        percentage = student['percentage']
        all_percentages.append(percentage)
    for student in students.keys():
        all_names.append(student)
    name_and_percent = list(zip(all_names, all_percentages))
    name_and_percent = sorted(name_and_percent, key = lambda x:x[1], reverse = True)
    return name_and_percent
    
def top(students):
    name_and_percent = rank(students)
    top_student = name_and_percent[0]
    return top_student

def clear(students):
    students.clear()
    sys.exit(0)

def seperate():        # Format function
    print('∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙')
    
def close():
    print('--------------------------------closing the program--------------------------------'.center(120))
    time.sleep(8)
    exit()
