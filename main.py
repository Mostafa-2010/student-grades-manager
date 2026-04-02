# The main file which contains all the features mentioned in the README.md file.

import json
import os
import time
from function import *    # Importing functions file


students = {}
valid_commands = ['create new', 'remove', 'top','rank', 'student info','clear', 'exit']
if os.path.exists('data.json'):      # To prevent error while reading the file if the file doesn't exist.
    with open('data.json', 'r') as f:
        students = json.load(f)
else:
    save(students)   # To create new empty file if The json file is not there.

while True:
    command = input(f'○ Enter a command:{valid_commands}: ').lower().strip()
    if command in valid_commands:
        if command == 'create new':
            create_n = input('♦ Enter the name of the student: ').lower().strip()
            create_e = input('♦ Enter the English degree from 0:100: ').strip()
            create_m = input('♦ Enter the Math degree from 0:100: ').strip()
            create_s = input('♦ Enter the science degree from 0:100: ').strip()
            create_b = input('♦ Enter the year of birth: ').strip()
            create_e, create_m, create_s, create_b = return_int(create_e, create_m, create_s, create_b)
            check = check_data(students, create_n, create_e, create_m, create_s, create_b)
            if check == 'valid data':
                percentage = calc_percentage(create_e, create_m, create_s)
                students = new_student(students, create_n, create_e, create_m, create_s, percentage, create_b)
                save(students)
                print('\n♦ Saved Successfully!')
                seperate()
            else:
                print(check,'\n♦ Please recheck your inputs!')
                seperate()
                continue;

        elif command == 'student info':
            while True:
                name_search = input("♦ Enter the student's name you want to view or tyrp 'return' to return to the menu: ")
                if name_search in students.keys():
                    student = show_student(students, name_search, students[name_search]['percentage'], students[name_search]['birth_year'])
                    print(f'    • Student name: {name_search}\n    • Year of birth: {student[4]}\n    • English grade: {student[0]}\n    • Math grade: {student[1]}\n    • Science grade: {student[2]}\n    • Percentage: {student[3]}%\n')
                    time.sleep(6)
                    seperate()
                    break;

                elif name_search == 'return':
                    break;

                else:
                    print('student not found, Please try again or return to the menu')
                    continue;

        elif command == 'remove':
            name_search = input('♦ Enter the student name you want to remove: ')
            if name_search in students.keys():
                student = show_student(students, name_search, students[name_search]['percentage'], students[name_search]['birth_year'])
                print(f'    • Student name: {name_search}\n    • Year of birth: {student[4]}\n    • English grade: {student[0]}\n    • Math grade: {student[1]}\n    • Science grade: {student[2]}\n    • Percentage: {student[3]}%\n')
                time.sleep(3)
                insurance = input('♦ Are you sure you want to remove that student Y/N: ').lower().strip()
                if insurance == 'y':
                    remove_student(students, name_search)
                    print(f'♦ {name_search} has been removed from the Database!')
                    seperate()
                    time.sleep(2)
                else:
                     print('♦ The deletion process was canceled!\n', f"♦ The info of the student {name_search} wasn't deleted")
                     seperate()
                     
        elif command == 'rank':
            name_percent = rank(students)
            rank_count = 1
            for name, percent in name_percent:
                print(f'    • {rank_count}) {name:12}  -{percent}%-') #since i gave a check for the name not to be more than 12 so i puted 12
                rank_count += 1
            seperate()
                
        elif command == 'top':
            top_student = top(students)
            name, percent = top_student
            print('------------------------------THE TOP STUDENT------------------------------'.center(120))
            print(f'○ {name.upper()}            {percent}%')
            seperate()

        elif command == 'clear':
            insurance = input('♦ ARE YOU SURE YOU WANT TO DELETE ALL THE DATA Y/N ?: ').lower().strip()
            if insurance == 'y':
                clear(students)
                print('♦ All the data has been cleared')
                seperate()
            else:
                print('♦ The operation was canceled!')
                seperate()
        elif command == 'exit':
            close()
            
    else:
        print('☼ PLEASE ENTER A VALID COMMAND:')
               
        
