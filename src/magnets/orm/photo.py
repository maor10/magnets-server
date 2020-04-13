from mongoengine import Document, ReferenceField, StringField

from magnets.orm.event import Event
from magnets.orm.user import User


class Photo(Document):

    creator = ReferenceField(User)
    event = ReferenceField(Event)
    file_name = StringField()
