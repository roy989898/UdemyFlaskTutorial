from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}

# 'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
userid_mapping = {u.id: u for u in users}


# 1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'asdf'
# }


def autjenticate(username, password):
    user = userid_mapping.get(username, None)
    if user is not None and safe_str_cmp(password, user.password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
