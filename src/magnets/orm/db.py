from mongoengine import connect


def connect_to_db():
    return connect('magnets')
