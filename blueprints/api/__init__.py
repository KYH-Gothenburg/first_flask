import json
from flask import Blueprint, request, Response
from controllers import user_controller
bp_api = Blueprint('bp_api', __name__)

# /users
# /users/2
# /users/2/messages
# /users/2/messages/3


@bp_api.get('/users')
def get_all_users():
    users = user_controller.get_all_users()
    cleaned_users = []
    for user in users:
        u = user.__dict__
        del u['_sa_instance_state']
        del u['recv_messages']
        cleaned_users.append(u)

    return Response(json.dumps(cleaned_users), 200, content_type='application/json')