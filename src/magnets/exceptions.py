
class MagnetsException(Exception):
    pass


class MagnetsClientException(MagnetsException):
    status_code = 400


class EntityNotFoundException(MagnetsClientException):

    status_code = 404

    def __init__(self, cls, entity_id, field=None):
        field = field or 'id'
        super(EntityNotFoundException, self).__init__(f"{cls.__name__} with {field} {entity_id} not found")
