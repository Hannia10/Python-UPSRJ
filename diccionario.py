import sys

students = [
{
    'name':'Hannia',
    'lastname':'Arias',
    'email':'Hannia@gmail.com'
},
{
    'name':'Vianney',
    'lastname':'Soto',
    'email':'Vianney@gmail.com'
}

]

def craete_student(student):
    global students
    if student not in students:
        students.append(student)
    else:
        print('Este vate ya esta registrade krnel')
    

def delete_student(student_name):
    global students
    student_delete = None
    for student in students:
        if student_name in student['name']:
          students.remove(student)
          student_delete = student
          break
    if not student_delete:
        print('Student {} is not in the students list'.format(student_name))


def update_student(student_name, student_updated):
    global students
    student_up = None
    for student in students:
        if student_name in student['name']:
            index = students.index(student)
            students[index] = student_updated
            student_up = student_updated_name
            break
    if not student_up:
        print('Este vate no estaba registrade krnel')


def search_student(student_name):
    global students
    for student in students:
        if student['name'] != student_name:
            continue
        else:
            return student


def _add_coma ():
    global students
    students += ','


def _get_student_field(field_name):
    field = None
    while not field:
        field = input('What is the student {}?'.format(field_name)).capitalize()
    return field


def _get_student_update(student_updated_field,student_name):
    student =search_student(student_name)
    if student:
        if student_updated_field == 'name':
            student['name'] = _get_student_field('name')
            return student
        elif student_updated_field == 'lastname':
            student['lastname'] = _get_student_field('lastname')
            return student
        elif student_updated_field == 'email':
            student['email'] = _get_student_field('email')
            return student
        elif student_updated_field == 'all':
            student['name'] = _get_student_field('name')
            student['lastname'] = _get_student_field('lastname')
            student['email'] = _get_student_field('email')
            return student
        else:
            return None



def _get_student_name ():
    student_name = None
    while not student_name:
        student_name = input('What is the student name?').capitalize()
        if student_name == 'Exit':
            student_name = None
            break
    if not student_name:
        sys.exit()
    return student_name


def list_students():
    global students
    for idx, student in enumerate(students):
        print('{idx} | {name} | {lastname} | {email}'.format(
            idx = idx,
            name = student['name'],
            lastname = student['lastname'],
            email = student['email']
            ))


def _print_welcome():
    print('Welcome to UPSRJ')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate student')
    print('[L]ist students')
    print('[D]elete student')
    print('[U]pdate student')
    print('[S]earch student')


if __name__ == "__main__": 
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        student = {
            'name': _get_student_field('name'),
            'lastname': _get_student_field('lastname'),
            'email': _get_student_field('email')
        }
        craete_student(student)
        list_students()
    elif command == 'D':
        student_name = _get_student_name()
        delete_student(student_name)
        list_students()
    elif command == 'U':
        student_name = _get_student_name()
        student_updated_field = input('What is the update student field? [name, lastname, email, all] ').lower()
        student_updated = _get_student_update(student_updated_field,student_name)
        if student_updated:
            update_student(student_name, student_updated)
            list_students()
        else:
            print('name or field invalid')
    elif command == 'L':
        list_students()
    elif command == 'S':
        student_name = _get_student_name()
        found = search_student(student_name)
        if found:
            print('The student: {} is in the student\'s list'.format(student_name))
        else:
            print('The student: {} is not in the student\'s list'.format(student_name))
    else:
        print('No se puede karnal')