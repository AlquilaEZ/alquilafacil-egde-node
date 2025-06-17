"""
Database initialization for the AlquilaFacil Edge Service.

Sets up the SQLite database and creates required tables for devices and health records.
"""
from peewee import SqliteDatabase

# Initialize SQLite database
db = SqliteDatabase('alquilafacil.db')

def init_db() -> None:
    """
    Initialize the database and create tables for Device and HealthRecord models.
    """
    db.connect()
    from locals.infrastructure.models import Local
    from management.infrastructure.models import Reading
    db.create_tables([Local, Reading], safe=True)
    db.close()