from mongoengine import Document, StringField, ReferenceField
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
