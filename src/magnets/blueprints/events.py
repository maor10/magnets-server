from bson import ObjectId
from flask import Blueprint
from mongoengine import DoesNotExist

from magnets.decorators import magnets_route
from magnets.exceptions import EntityNotFoundException
from magnets.orm.event import Event
from magnets.orm.user import User

events_blueprint = Blueprint('events', __name__)


@magnets_route(events_blueprint, '/', methods=['POST'])
def create_event(user_id, name):
    user_id = ObjectId(user_id)
    try:
        user = User.objects.filter(id=user_id).get()
    except DoesNotExist:
        raise EntityNotFoundException(User, user_id)
    Event.create(name=name, creator=user).save()


@magnets_route(events_blueprint, '/', methods=['GET'])
def get_events():
    return [event.to_client_json() for event in Event.objects.all()]


@magnets_route(events_blueprint, '/<string:event_id>', methods=['GET'])
def get_event(event_id):
    try:
        event = Event.objects.filter(id=ObjectId(event_id)).get()
    except DoesNotExist:
        raise EntityNotFoundException(Event, event_id)
    return event.to_client_json()


@magnets_route(events_blueprint, '/with_code', methods=['GET'])
def get_event_by_code(code):
    try:
        event = Event.objects.filter(code=code).get()
    except DoesNotExist:
        raise EntityNotFoundException(Event, code, field='code')
    return event.to_client_json()
