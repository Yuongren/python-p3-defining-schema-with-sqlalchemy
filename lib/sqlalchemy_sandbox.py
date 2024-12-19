from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    # Create an SQLite database engine
    engine = create_engine('sqlite:///students.db')

    # Create the 'students' table if it doesn't exist
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if a student record with the name 'John Doe' already exists
    john_doe = session.query(Student).filter_by(name='John Doe').first()

    if not john_doe:
        # Insert a new student record
        new_student = Student(name='John Doe')
        session.add(new_student)
        session.commit()
        print("New student added.")

    # Check if a student record with the name 'Brian Kamau' already exists
    brian_kamau = session.query(Student).filter_by(name='Brian Kamau').first()

    if not brian_kamau:
        # Insert another new student record
        old_student = Student(name='Brian Kamau')
        session.add(old_student)
        session.commit()
        print("Another student added.")

    # Query and print all student records
    students = session.query(Student).all()
    print("List of Students:")
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")

    # Close the session
    session.close()