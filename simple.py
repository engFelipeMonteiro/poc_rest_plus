from flask import Flask
from simple_page import simple_page
from other_page import other_page
from flask_restplus import Api

app = Flask(__name__)
api = Api(simple_page, doc='/doc/')


app.register_blueprint(simple_page)
#app.register_blueprint(simple_page, url_prefix='/simple_page')
app.register_blueprint(other_page, url_prefix='/other_page')
app.run()
#import pdb; pdb.set_trace()
