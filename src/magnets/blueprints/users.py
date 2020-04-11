from flask import Blueprint

from magnets.decorators import magnets_route
from magnets.orm.user import User

users_blueprint = Blueprint('users', __name__)


@magnets_route(users_blueprint, '/', methods=['POST'])
def create_user(uuid):
    user = User(uuid=uuid)
    user.save()
