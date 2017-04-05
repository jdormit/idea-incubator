from database.db import db
from database.entities import *

def init_db():
    db.bind('postgres', user='idea_incubator_safeuser', password='password', host='localhost', database='idea_incubator')
    db.generate_mapping(create_tables=True)
