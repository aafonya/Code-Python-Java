from peewee import *
from utility.filereader import FileReader


fileread = FileReader()
database_name = fileread.database_name()
database_user = fileread.database_user()


db = PostgresqlDatabase(database_name, user=database_user)


class BaseModel(Model):

    class Meta:
        database = db


class OurModel(BaseModel):

    name = CharField()
    title = CharField()

db.connect()

db.drop_tables([OurModel], safe=True)

# List the tables here what we want to create
db.create_tables([OurModel], safe=True)
