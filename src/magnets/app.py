from flask import Flask

from magnets.blueprints.events import events_blueprint
from magnets.blueprints.users import users_blueprint
from magnets.decorators import magnets_route
from magnets.orm.db import connect_to_db

app = Flask(__name__)

app.register_blueprint(events_blueprint, url_prefix='/events')
app.register_blueprint(users_blueprint, url_prefix='/users')


@magnets_route(app, '/ping')
def pong():
    return 'pong'


if __name__ == '__main__':
    connect_to_db()
    app.run(debug=True)
