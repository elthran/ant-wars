from flask import Blueprint

# FIXME: This should use dynamic import and composition
# as all the imports and setup with be very similar.
from ..api.world_controller import WorldController

api_blueprint = Blueprint('api', __name__, url_prefix='/api')


api_blueprint.add_url_rule('/world/<int:id>', view_func=WorldController.as_view('world_controller'))
# api_blueprint.add_url_rule('/colony/<int:_id>', view_func=ColonyController.as_view('colony_controller'))
# api_blueprint.add_url_rule('/colony/<int:_id>', view_func=AntController.as_view('ant_controller'))
