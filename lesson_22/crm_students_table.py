from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from orm_base_table import Base


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer,   primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, nullable=True)

    # Встановлення відношення "багато до одного" з таблицею Relations
    relations = relationship("Relations", back_populates="student")


    def __str__(self):
        return f'id:{self.id}, name:{self.name}, email:{self.email}'