from peewee import Model, AutoField, IntegerField, CharField, DateTimeField
from shared.infrastructure.database import db

class Reading(Model):
  """
  ORM model for readings table.
  Represents a reading entity in the database.
  """
  id = AutoField()
  local_id = IntegerField(null=False)
  sensor_type = CharField(max_length=50, null=False)
  message = CharField(max_length=255, null=False)
  timestamp = DateTimeField(null=False)

  class Meta:
    """
    Meta class for Reading.
    Defines the database table name and other configurations.
    """
    table_name = 'readings'
    database = db