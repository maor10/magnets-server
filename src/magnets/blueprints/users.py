from flask import Blueprint
from mongoengine import DoesNotExist

from magnets.blueprints import utils
from magnets.decorators import magnets_route
from magnets.exceptions import EntityNotFoundException
from magnets.orm.event import Event
from magnets.orm.user import User
from magnets.orm.user_event import UserEvent

users_blueprint = Blueprint('users', __name__)


@magnets_route(users_blueprint, '/', methods=['POST'])
def create_user(uuid):
    user = User(uuid=uuid)
    user.save()


@magnets_route(users_blueprint, '/', methods=['GET'])
def get_users():
    return [user.to_client_json() for user in User.objects.all()]


@magnets_route(users_blueprint, '/<string:user_id>/join_event/<string:event_id>', methods=['POST'])
def join_event(user_id, event_id):
    user = utils.get_user_by_id(user_id)
    event = utils.get_event_by_id(event_id)
    UserEvent(user=user, event=event).save()
