from mongoengine import Document, StringField


class User(Document):
    uuid = StringField()

    def to_client_json(self):
        return {
            'id': str(self.id),
            'uuid': str(self.uuid)
        }
