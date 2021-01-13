import sys

students = ['Hannia', 'Roberto']

def delete_student(student_name):
    global students
    if student_name in students:
        students.pop(students.index(student_name))
        print(students)
    else:
        print('The student is not in the list')

def update_student(student_name, new_student):
    global students
    new_student = new_student.capitalize()
    if student_name in students:
        posicion=students.index(student_name)
        students.pop(students.index(student_name))
        students.insert(posicion, new_student)
        print(students)
    else:
        print('It is not in the students list')

def get_student_name ():
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
    student_name= student_name.capitalize()
    if student_name in students:
        print('The student is in the list')
        return True
    else:
        print('The student is not in the list')
        return False

#    def list_student():
#        global student
#        for idx, student in enumerate(students): para que al momento de imprimir aparezca la posicion 
#            print("{} : {}".format(idx, student))


def _print_welcome_():
    print('welcome to upsrj?')
    print('*' * 50)
    print('what would you like to do today?')
    print('[C]reate student')
    print('[U]pdate student')
    print('[D]elete student')
    print('[L]ist student')
    print('[S]earch student')

if __name__ == "__main__":
    _print_welcome_()
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
        

    elif command == 'D':
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
else:
    print ('No hay nada que hacer aqui, thank u, next')