# Articles Without SQLAlchemy

A simple Python project for managing articles, authors, and magazines using SQLite, without using SQLAlchemy ORM. This project demonstrates basic CRUD operations, relationships, and database seeding using raw SQL and Python classes.


## Setup

1. **Install dependencies**  
   This project uses Python 3.12 and `pytest` for testing. Install dependencies with pipenv:
   ```sh
   pipenv install --dev

2. #  Set up the database schema
Run the setup script to create the SQLite database and tables:
    (python scripts/setup.py)

3. # Seed the database
Populate the database with sample data:
 (python scripts/seed_db.py)

4. # Running Tests
Unit tests are located in test. Run all tests with:
  pytest

# Usage
# Models:

   lib.models.article.Article: Represents an article.
   lib.models.author.Author: Represents an author.
   lib.models.magazine.Magazine: Represents a magazine.
# Database:

   lib.models.db.connection: Handles SQLite connections.
    lib.models.db.schema.sql: Defines the database schema.
    lib.models.db.seed: Seeds the database with sample data.
# Scripts:

   setup_db.py: Sets up the database schema.
   seed_db.py: Seeds the database.
# Interactive Debugging
  You can use the debug console to interact with models:
  (python lib/models/db/debug.py)
   Type show_help() in the console for available commands.


