import os
import random

from faker import Faker
from sqlalchemy import create_engine, update, delete, text
from sqlalchemy.orm import sessionmaker
from crm_courses_table import Courses
from crm_students_table import Students
from crm_stud_course_relat import Relations
from orm_base_table import Base

if os.path.exists("test_db.sqlite"):
    os.remove("test_db.sqlite")

faker = Faker()

engine = create_engine("sqlite:///test_db.sqlite")

with engine.connect() as conn:
    conn.execute(text('PRAGMA foreign_keys = ON;'))

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# аналог insert
students = [
    Students(
        name=f'test-{faker.name()}',
        email=faker.email()
    )
    for k in range(20)
]
session.add_all(students)

courses = [
    Courses(name='Python'),
    Courses(name='JavaScript'),
    Courses(name='Java'),
    Courses(name='C#'),
    Courses(name='PHP'),
]
session.add_all(courses)

relations = []
student_ids = list(range(1, 16))
course_ids = list(range(1, 6))

for student_id in student_ids:
    courses_amount = random.randint(0, 5)

    if courses_amount == 0:
        continue

    selected_courses = random.sample(course_ids, courses_amount) # i from n courses
    for course_id in selected_courses:
        relations.append(Relations(student_id=student_id, course_id=course_id))
session.add_all(relations)

session.commit()

new_student = Students(name='Alex Smith', email='alex.smith@example.com')
session.add(new_student)
session.commit()

selected_course = session.query(Courses).filter(Courses.name == 'Python').first()

if new_student and selected_course:
    relation = Relations(student=new_student, course=selected_course)
    session.add(relation)
    session.commit()
    print(f"Student {new_student.name} added to course {selected_course.name}")
else:
    print("Error: student or course are missing in table")

students_on_course = (
    session.query(Students.name, Students.email).join(Relations).join(Courses).filter(Courses.name == 'JavaScript').all())

for s in students_on_course:
    print(f"JavaScript student:{s.name} — {s.email}")

courses_for_student = (session.query(Courses.name).join(Relations).join(Students).filter(Students.name == 'Alex Smith').all())

for course in courses_for_student:
    print(f"Alex Smith attend course: {course.name}")


student_to_update = session.query(Students).filter(Students.name == 'Alex Smith').first()
if student_to_update:
    student_to_update.name = 'Rick Newman'
    student_to_update.email = 'rick.newman@example.com'
    session.commit()

selected_stud = session.query(Students).filter(Students.name == 'Rick Newman').first()
print(f'Updated user data: ID={selected_stud.id}, Name={selected_stud.name}, Email={selected_stud.email}')

delete_query = delete(Students).where(Students.name == 'Rick Newman')
session.execute(delete_query)
session.commit()

deleted_student_check = session.query(Students).filter(Students.name == 'Rick Newman').first()

if deleted_student_check is None:
    print("Rick Newman was successfully deleted.")
else:
    print("Rick Newman still exists in the database.")

session.close()

