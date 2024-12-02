from typing import Generator
from app.database import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Generator[Session]:
    """
    Opens a database session and closes it when a operation is finished.

    Yields:
        Generator[Session]: Generates a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
