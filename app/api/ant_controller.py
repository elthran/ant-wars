from flask import request, jsonify
from flask.views import MethodView

from ..models.ants import Ant
from ..serializers.ant_serializer import AntSerializer

import pdb


class AntController(MethodView):

    def get(self, id_):
        ant = Ant.query.get(id_)
        return jsonify(
            ant=AntSerializer.render(ant)
        )

    def put(self, id_):
        ant = Ant.query.get(id_)
        # pdb.set_trace()
        attributes = request.json
        updated_ant = ant.update(attributes)
        # Add security here
        return jsonify(
            ant=AntSerializer.render(updated_ant)
        )

