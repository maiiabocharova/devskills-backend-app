# removing existing databas and creating everything from scratch
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///credit.db")

# Create a DeclarativeMeta instance
Base = declarative_base()


class Credit(Base):
    __tablename__ = 'credits'

    ssn = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    assessed_income = Column(Integer)
    balance_of_debt = Column(Integer)
    complaints = Column(Boolean)

    def __repr__(self):
        return f"<Person with ssn={self.id} and name={self.first_name}>"

Base.metadata.create_all(engine)