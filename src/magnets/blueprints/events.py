import os
import uuid

from flask import Blueprint, request
from werkzeug.datastructures import FileStorage

from magnets.blueprints import utils
from magnets.consts import UPLOAD_FOLDER
from magnets.decorators import magnets_route
from magnets.orm.event import Event
from magnets.orm.photo import Photo

events_blueprint = Blueprint('events', __name__)


@magnets_route(events_blueprint, '/', methods=['POST'])
def create_event(user_id, name):
    user = utils.get_user_by_id(user_id)
    event = Event.create(name=name, creator=user).save()
    return event.to_client_json()


@magnets_route(events_blueprint, '/', methods=['GET'])
def get_events():
    return [event.to_client_json() for event in Event.objects.all()]


@magnets_route(events_blueprint, '/<string:event_id>', methods=['GET'])
def get_event(event_id):
    event = utils.get_event_by_id(event_id)
    return event.to_client_json()


@magnets_route(events_blueprint, '/with_code', methods=['GET'])
def get_event_by_code(code):
    event = utils.get_object_by_field(Event, field_name='code', field_value=code)
    return event.to_client_json()


@magnets_route(events_blueprint, '/<string:event_id>/photos', methods=['GET'])
def get_event_photos(event_id):
    event = utils.get_event_by_id(event_id)
    return [photo.to_client_json() for photo in event.get_photos()]


@magnets_route(events_blueprint, '/<string:event_id>/photos', methods=['POST'])
def create_photo(event_id):
    user_id = request.form['user_id']
    user = utils.get_user_by_id(user_id=user_id)
    event = utils.get_event_by_id(event_id)
    photo_file: FileStorage = request.files['file']
    ext = photo_file.filename.rsplit(".", 1)[1]
    # TODO make sure it's an allowed extension
    file_name = f"{str(uuid.uuid4())}.{ext}"
    photo_file.save(os.path.join(UPLOAD_FOLDER, file_name))
    photo = Photo(
        creator=user,
        event=event,
        file_name=file_name
    ).save()
    return photo.to_client_json()
