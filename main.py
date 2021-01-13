#.upper (Mayuscula)
#.lower(Minuscula)



#Se inicializa el codigo

#DESPUES DE UN if, DAR UNA TABULACIÓN (4 ESPACIOS)

#pass = bloque de codigo vacio

#Para ser variable global necesita estar dentro de un metodo

import sys

students = "Hannia,Diego,"

def _add_comma():
    global students
    students += ","


def get_student_name():
    student_name = None
    while not student_name:
        student_name = input ('What is the student Name?').capitalize()
        if student_name == 'Exit':
            student_name = None
            break
    if not student_name:
        sys.exit()
    return student_name


def create_student(student_name):
    global students
    student_name = student_name.capitalize()
    if student_name not in students:
        students += student_name
        _add_comma() # cuando empieza con _ es una privada
    else:
        print("Este vato ya está registrado")

def list_students (): 
    global students
    print(students)

def _delete_student (student_name):
    global students
    if student_name in student_name:
        students = students.replace(student_name + ',' , '')
    else:
        print('Sudent {} is not in the students list'.format(student_name))    

def update_student (student_name, student_update_name): 
    global students
    print (student_name)
    if student_name in students:
        students = students.replace(student_name , student_update_name)
        
    else:
        print ('Student is not in the students list')


def _print_welcome():
    print("welcome to upsrj")
    print("*" * 50)
    print("what would you like to do today")
    print("[c]reate student")
    print("[D]elete student")
    print("[A]ctualizar student")
    print("[L]ist students")
    print("[S]earch students")

def search_student (student_name):
    global students
    students_list = students.split(',')
    for student in students_list:
        if student != student_name:
            continue
        else:
            return True



if __name__ == "__main__":
    _print_welcome()
    variable = input()
    variable = variable.upper()
    if variable == "C":
        student_name = get_student_name()
        create_student(student_name)
        list_students()
    elif variable == "D":
        student_name = get_student_name()
        _delete_student(student_name)
        list_students()
    elif variable == "A":
        student_name = get_student_name()
        student_update_name = input ('What is the update student name?').capitalize()
        update_student(student_name, student_update_name)
        list_students()
    elif variable == 'L':
        list_students()
    elif variable == 'S':
        student_name = get_student_name()
        found = search_student(student_name)
        if found:
            print ('The student: {} is in the student\'s list'.format(student_name))
        else:
            print('The student: {} is not in the student\'s list'.format(student_name))

    else:
        print("no se puede krnal")
    