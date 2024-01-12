import click
from sqlalchemy import create_engine

from model import  Teacher, Student, Grade, session
from algorithms import calculate_average_grade

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter teacher\'s name', help='Teacher\'s name')
@click.option('--subject', prompt='Enter subject', help='Subject taught by the teacher')
def add_teacher(name, subject):
    teacher = Teacher(name=name, subject=subject)
    session.add(teacher)
    session.commit()
    click.echo(f'Teacher {name} teaching {subject} added.')

@cli.command()
@click.option('--name', prompt='Enter student\'s name', help='Student\'s name')
@click.option('--grade', prompt='Enter student\'s grade', help='Student\'s grade')

def add_student(name, grade):
    student = Student(name=name, grade=grade)
    session.add(student)
    session.commit()
    click.echo(f'Student {name} in grade {grade} added.')

@cli.command()
@click.option('--student_name', prompt='Enter student\'s name', help='Student\'s name')
@click.option('--subject', prompt='Enter subject', help='Subject for the grade')
@click.option('--value', prompt='Enter grade value', help='Grade value')
def assign_grade(student_name, subject, value):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        grade = Grade(subject=subject, value=value, student=student)
        session.add(grade)
        session.commit()
        click.echo(f'Grade {value} assigned to {student_name} in {subject}.')
    else:
        click.echo(f'Student {student_name} not found.')

@cli.command()
def display_info():
    click.echo("\nTeachers:")
    for teacher in session.query(Teacher).all():
        click.echo(f'{teacher.name} - {teacher.subject}')
        for student in teacher.students:
            average_grade = calculate_average_grade(student)
            click.echo(f'  Student: {student.name} - Average Grade: {average_grade}')

    click.echo("\nStudents:")
    for student in session.query(Student).all():
        click.echo(f'{student.name} - Grade: {student.grade}')
        click.echo('  Grades:')
        for grade in student.grades:
            click.echo(f'    {grade.subject}: {grade.value}')
#display_info()
if __name__ == "__main__":
    cli()