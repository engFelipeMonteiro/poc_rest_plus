#restplus based artecture
from flask import Blueprint, render_template, abort, Flask
from jinja2 import TemplateNotFound
app = Flask(__name__)

other_page = Blueprint('other_page', __name__)

from flask_restplus import Api, Resource, fields

api = Api(other_page, version='1.0', title='Todo API',
    description='A simple TODO API', doc='/doc/', template_folder='templates',
)


@api.route('/')
class TodoSimple(Resource):
    def get(self):
        try:
            return render_template('other_page.html')
        except TemplateNotFound:
            abort(418)

