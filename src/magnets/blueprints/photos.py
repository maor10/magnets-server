from flask import Blueprint, send_from_directory

from magnets.blueprints import utils
from magnets.consts import UPLOAD_FOLDER
from magnets.decorators import magnets_route

photos_blueprint = Blueprint('photos', __name__)


@magnets_route(photos_blueprint, '/<string:photo_id>')
def get_photo(photo_id):
    photo = utils.get_photo_by_id(photo_id)
    return photo.to_client_json()


@magnets_route(photos_blueprint, '/<string:photo_id>/image', dump_as_json=False)
def get_photo_image(photo_id):
    photo = utils.get_photo_by_id(photo_id)
    return send_from_directory(UPLOAD_FOLDER, photo.file_name)
