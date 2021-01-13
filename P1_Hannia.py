import sys
students = ['Hania','Diego','Robert']


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
    if student_name not in students:
        students.append(student_name)
    else:
        print("Alumno registrado")

def list_students (): 
    global students
    print(students)

def search_student(student_name):
    global students
    student_name= student_name.capitalize()
    if student_name in students:
        print('Alumno existente')
    else:
        print('Alumno inexistente')
        

def _delete_student (student_name):
    global students
    if student_name in students:
        students.remove(student_name)
    else:
        print('Sudent {} is not in the students list'.format(student_name))    
def update_student (student_name, student_update_name): 
    global students
    student_update_name = student_update_name.capitalize()
    if student_name in students:
        position = students.index(student_name)
        students.remove(position)
        students.insert(position, student_update_name)        
    else:
        print ('Student {} is not in the students list'.format(student_name))


def _print_welcome():
    print("welcome to upsrj")
    print("*" * 50)
    print("what would you like to do today")
    print("[c]reate student")
    print("[D]elete student")
    print("[A]ctualizar student")
    print("[L]ist students")
    print("[S]earch students")




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
        search_student(student_name)
    

    else:
        print("no se puede krnal")


  