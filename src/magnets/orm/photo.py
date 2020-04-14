from mongoengine import Document, ReferenceField, StringField

from magnets.orm.event import Event
from magnets.orm.user import User


class Photo(Document):

    creator = ReferenceField(User)
    event = ReferenceField(Event)
    file_name = StringField()

    def to_client_json(self):
        return {
            'id': self.id,
            'creator_id': self.creator.id,
            'event_id': self.event.id,
        }
