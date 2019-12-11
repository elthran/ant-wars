from flask import request, jsonify
from flask.views import MethodView

from ..models.worlds import World
from ..serializers.world_serializer import WorldSerializer


class WorldController(MethodView):

    def get(self, id):
        world = World.query.get(id)
        return jsonify(
            world=WorldSerializer.render(world)
        )

    def put(self, id):
        world = World.query.get(id)
        attributes = request.json
        updated_world = world.update(attributes)
        # Add security here
        return jsonify(
            world=WorldSerializer.render(updated_world)
        )

