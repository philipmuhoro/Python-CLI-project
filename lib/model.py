from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///school.db", echo=True)
Session= sessionmaker(bind=engine)
session=Session()

teacher_student_association = Table(
      'teacher_student_association', Base.metadata,
       Column('teacher_id', Integer, ForeignKey('teachers.id')),
       Column('student_id', Integer, ForeignKey('students.id'))
 )


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    students = relationship('Student', secondary=teacher_student_association, back_populates='teachers')
    
    def __repr__(self):
        return f" Name: {self.name} Subject: {self.subject} Student: {self.students}"


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)
    grades = relationship('Grade', back_populates='student')
    teachers = relationship('Teacher', secondary=teacher_student_association, back_populates='students')
    
    def __repr__(self):
        return f"Name: {self.name} Grade: {self.grade} Grades: {self.grades} {self.teachers}"

class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True)
    subject = Column(String)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship('Student', back_populates='grades')
    
    def __repr__ (self):
        return f"({self.id} {self.student} {self.value} {self.student_id} {self.student})"
        
