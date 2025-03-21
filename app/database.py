import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up logging for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # DEBUG level for detailed info

# PostgreSQL connection string; update with your credentials
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/healthcare_db"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
logger.info("Database engine created successfully.")

# Create a configured "Session" class.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logger.debug("SessionLocal configured.")
