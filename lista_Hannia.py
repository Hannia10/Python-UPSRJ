import sys

students = ['Hannia', 'Roberto', 'Santiago']

def _add_comma_():
    global students
    students += ","

def delete_student(student_name):
    global students
    if student_name in students:
        student.pop(students.index(student_name))
        print(students)
    else:
        print('It is not in the student list')

def update_student(student_name):
    global students
    if student_name in students:
        posicion = students.index(student_name)
        students.pop(posicion)
        students.insert(posicion, new_student)
        print(students)
    else:
        print('It is not in the students list')

def get_student_name (student):
    student_name = None
    while not student_name:
        student_name =input('what is the student name?').capitalize()
        if student_name == 'Exit':
            student_name=None 
            break
    if not student_name:
        sys.exit()
    return student_name

def search_student(student_name):
    global students
    student_name = student_name.capitalize()
    for student_name in students:
        if student != student_name:
            continue
        else:
            return True

def _welcome_():
    print("welcome to upsrj")
    print("*" * 50)
    print("what would you like to do today?")
    print("[c]reate student")
    print("[D]elete student")
    print("[U]pdate student")
    print("[L]ist students")
    print("[S]earch students")

if __name__ == "__main__":
    _welcome_()
    command = input()
    command = command.upper()
    if command == 'C': 
        for get_student_name in students:
            student = None
            student = input ("What's the new student name?").capitalize()
            students.append(student)
            print (students)
            student = student.capitalize()
            if student == 'Exit':
                break
            if not student:
                 sys.exit()
                 break

    elif command == 'D':
        student = input ("Which one do you want to delete?")
        student_name=get_student_name()
        delete_student(student_name)

    elif command == 'U':
        student_name = get_student_name()
        if student_name in students:
            new_student=input('who is the new student?')
            new_student = new_student.capitalize()
            update_student(student_name, new_student)
        
        else:
            print('It doesnt exist')

    elif command == 'L':
        print (students)

    elif command == 'S':
        student_name = get_student_name()
        search_student(student_name)