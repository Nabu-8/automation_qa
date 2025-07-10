from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from orm_base_table import Base


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Встановлення відношення "багато до одного" з таблицею Relations
    relations = relationship("Relations", back_populates="course")

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'
