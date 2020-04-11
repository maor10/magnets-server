from mongoengine import Document, StringField


class User(Document):
    uuid = StringField()
