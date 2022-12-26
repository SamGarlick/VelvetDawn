import velvet_dawn
from flask import Blueprint, request

from config import Config
from velvet_dawn.models.phase import Phase

setup_blueprint = Blueprint('setup_blueprint', __name__)

config = Config().load()


@setup_blueprint.route("/", methods=["POST"])
def update_game_setup():
    # TODO verify admin
    player = request.form.get("username")

    entity_id = request.form.get("entity")
    count = int(request.form.get("count"))

    velvet_dawn.game.setup.update_setup(entity_id, count)

    return velvet_dawn.game.setup.get_setup(player).json()


@setup_blueprint.route("/add/", methods=["POST"])
def add_entity_during_setup():
    # TODO verify player
    player = request.form.get("username")
    entity = request.form.get("entity")
    x = int(request.form.get("x"))
    y = int(request.form.get("y"))

    velvet_dawn.game.setup.place_entity(player, entity, x, y)

    return velvet_dawn.game.get_state(config, player).json()


@setup_blueprint.route("/remove/", methods=["POST"])
def remove_entity_during_setup():
    # TODO verify player
    player = request.form.get("username")
    x = int(request.form.get("x"))
    y = int(request.form.get("y"))

    velvet_dawn.game.setup.remove_entity(player, x, y)

    return velvet_dawn.game.get_state(config, player).json()


@setup_blueprint.route("/start-setup/", methods=["POST"])
def start_game_setup():
    # TODO verify player is admin
    player = request.args.get("username")

    if velvet_dawn.game.phase.get_phase() == Phase.Lobby:
        velvet_dawn.game.phase.start_setup_phase(config)

    return velvet_dawn.game.get_state(config, player).json()