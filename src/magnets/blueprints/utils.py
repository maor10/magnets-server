from typing import Type

from bson import ObjectId
from mongoengine import DoesNotExist, Document

from magnets.exceptions import EntityNotFoundException
from magnets.orm.event import Event
from magnets.orm.user import User


def get_object_by_field(cls: Type[Document], field_name: str, field_value: any):
    """
    Get a singular object by a given field and value, raising EntityNotFound if not found

    :param cls: to query
    :param field_name: to query
    :param field_value: of object searching for
    :raises EntityNotFoundException
    :return: object of type cls
    """
    try:
        return cls.objects.filter(**{field_name: field_value}).get()
    except DoesNotExist:
        raise EntityNotFoundException(cls, field_value, field=field_name)


def get_event_by_id(event_id: str) -> Event:
    """
    Get an event by a given id

    :param event_id: of event
    :raises EntityNotFoundException
    :return: Event
    """
    return get_object_by_field(Event, 'id', ObjectId(event_id))


def get_user_by_id(user_id: str) -> User:
    """
    Get an event by a given id

    :param user_id: of user
    :raises EntityNotFoundException
    :return: User
    """
    return get_object_by_field(User, 'id', ObjectId(user_id))
