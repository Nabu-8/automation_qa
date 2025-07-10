from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base_table import Base


class Relations(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    course_id = Column(Integer, ForeignKey('courses.id', ondelete='CASCADE'))


    # Встановлення відношення "багато до одного" з таблицею Students
    student = relationship("Students", back_populates="relations")
    # Встановлення відношення "багато до одного" з таблицею Courses
    course = relationship("Courses", back_populates="relations")


    def __str__(self):
        return f'id: {self.id}, student_id: {self.student_id}, course_id:{self.course_id}'