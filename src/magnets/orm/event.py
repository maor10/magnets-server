from mongoengine import Document, StringField, ReferenceField, ListField
import uuid
from magnets.orm.user import User


class Event(Document):

    name = StringField()
    creator = ReferenceField(User)
    code = StringField()

    @classmethod
    def create(cls, name, creator):
        code = str(uuid.uuid4())
        return cls(name=name, creator=creator, code=code)

    def to_client_json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'user_id': str(self.creator.id),
            'code': self.code
        }

    def get_users(self):
        from magnets.orm.user_event import UserEvent
        user_events = UserEvent.objects.find(event_id=self.id)
        return User.objects.filter(id__in=[user_event.user_id for user_event in user_events])

    def get_photos(self):
        from magnets.orm.photo import Photo
        return Photo.objects.filter(event=self)
