from flask import Blueprint

blueprint = Blueprint('index', __name__, url_prefix='/')

@blueprint.route('/')
@blueprint.route('/index')
def index():
    return "CARD FRAUD DETECTION API - INDEX BLUEPRINT"
