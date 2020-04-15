from mongoengine import Document, ReferenceField, StringField

from magnets.orm.event import Event
from magnets.orm.user import User


class Photo(Document):

    creator = ReferenceField(User)
    event = ReferenceField(Event)
    file_name = StringField()

    def to_client_json(self):
        return {
            'id': str(self.id),
            'creator_id': str(self.creator.id),
            'event_id': str(self.event.id),
        }
