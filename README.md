# Python-CLI-project
# School Management System CLI

The School Management System CLI is a command-line application that allows users to manage teachers, students, and grades in a school. The application is built using Python and leverages SQLAlchemy for database interaction, Alembic for database migrations, and includes algorithms for calculating average grades.

## Features

- Add teachers and students to the system.
- Assign grades to students for different subjects.
- Display information about teachers, students, and their grades.
- Use SQLAlchemy ORM for efficient database operations.
- Implement database migrations with Alembic to handle schema changes.

## Prerequisites

- Python 3.x
- Pipenv (for managing the virtual environment)
- Click
- Alembic
- SQLalchemy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/philipmuhoro/Python-CLI-project-cli.git
   
2. Navigate into the project
   ``` 
    cd Python-CLI-project
   ```

3. Install dependencies: 
   ``` 
   pipenv install
 
   ```
4. Set up the database
   ```
   # Create database and tables
   pipenv run python create_initial_data.py

   # Generate and apply migrations
   pipenv run alembic revision --autogenerate -m "Initial migration"
   pipenv run alembic upgrade head

   ```
## Usage
1. Activate the virtual environment:
   ```
   pipenv shell
   ```
2. Run the CLI application:
   ```
   pipenv run python cli.py
   ```

## Commands
- add_teacher: Add a new teacher to the system.
- add_student: Add a new student to the system.
- assign_grade: Assign a grade to a student for a specific subject.
- display_info: Display information about teachers, students, and their grades.

## Author and Licence
Philip Muhoro & [MIT LICENCE](LICENSE)