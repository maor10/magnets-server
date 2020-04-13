from mongoengine import Document, ReferenceField

from magnets.orm.event import Event
from magnets.orm.user import User


class UserEvent(Document):
    user = ReferenceField(User)
    event = ReferenceField(Event)
