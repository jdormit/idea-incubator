from datetime import datetime
from pony.orm import *
from database.db import db

class Idea(db.Entity):
    name = Required(str)
    summary = Required(str)
    description = Required(str)
    creator = Required(lambda: User, reverse="created_ideas")
    collaborators = Set(lambda: User, reverse="collaborator_ideas")
    discussions = Set(lambda: Discussion)
    create_datetime = Required(datetime)
    tags = Set(lambda: Tag)

class Tag(db.Entity):
    description = Required(str)
    ideas = Set(lambda: Idea)

class User(db.Entity):
    email = Required(str, unique=True)
    password = Required(str)
    collaborator_ideas = Set(lambda: Idea, reverse="collaborators")
    created_ideas = Set(lambda: Idea, reverse="creator") 
    discussions_participating = Set(lambda: Discussion, reverse="users")
    discussions_created = Set(lambda: Discussion, reverse="creator")
    posts = Set(lambda: DiscussionPost)

class Discussion(db.Entity):
    title = Required(str)
    creator = Required(lambda: User)
    idea = Required(lambda: Idea)
    create_datetime = Required(datetime)
    users = Set(lambda: User)
    posts = Set(lambda: DiscussionPost)

class DiscussionPost(db.Entity):
    discussion = Required(lambda: Discussion)
    parent = Optional(lambda: DiscussionPost)
    children = Set(lambda: DiscussionPost)
    author = Required(lambda: User)
    text = Required(str)
    post_datetime = Required(datetime)
    modify_datetime = Required(datetime)
