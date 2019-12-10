from flask import request, jsonify
from flask.views import MethodView

from ..models.colonies import Colony
from ..serializers.colony_serializer import ColonySerializer

import pdb


class ColonyController(MethodView):

    def get(self, id):
        colony = Colony.query.get(id)
        return jsonify(
            colony=ColonySerializer.render(colony)
        )

    def put(self, id):
        colony = Colony.query.get(id)
        # pdb.set_trace()
        attributes = request.json
        updated_colony = colony.update(attributes)
        # Add security here
        return jsonify(
            colony=ColonySerializer.render(updated_colony)
        )

