from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

DATABASE_URI = "mysql+pymysql://root:69596959@localhost/oz_main_project"

try:
    engine = create_engine(DATABASE_URI)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful!")
        print(f"Result of SELECT 1: {result.scalar()}")
except OperationalError as e:
    print(f"Database connection failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
