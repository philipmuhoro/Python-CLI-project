# create_initial_data.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.model import Base, Teacher, Student, Grade

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data
teacher1 = Teacher(name="Jon Snow", subject="History")
teacher2 = Teacher(name="Arya Stark", subject="Kiswahili")

student1 = Student(name="Cersei Lanister", grade="4")
student2 = Student(name="Daenerys Targaryen", grade="5")

grade1 = Grade(subject="History", value=90, student=student1)
grade2 = Grade(subject="Kiswahili", value=85, student=student2)

teacher1.students.append(student1)
teacher2.students.append(student2)

session.add_all([teacher1, teacher2])
session.commit()
