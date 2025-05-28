import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.db.seed import seed_database

if __name__ == "__main__":
    print("Starting database seeding...")
    seed_database()