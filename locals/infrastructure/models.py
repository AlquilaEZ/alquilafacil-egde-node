from peewee import Model, AutoField, IntegerField
from shared.infrastructure.database import db

class Local(Model):
  """
  ORM model for locals table.
  Represents a local entity in the database.
  """
  id = AutoField()
  capacity = IntegerField(null=False)

  class Meta:
    """
    Meta class for Local.
    Defines the database table name and other configurations.
    """
    table_name = 'locals'
    database = db