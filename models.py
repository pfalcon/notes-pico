import datetime

from flask import Markup
from markdown import markdown
from peewee import *

from app import db

class Note(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    archived = BooleanField(default=False)

    class Meta:
        database = db

    def html(self):
        return Markup(markdown(self.content))

    @classmethod
    def public(cls):
        return (Note
                .select()
                .where(Note.archived == False)
                .order_by(Note.timestamp.desc()))