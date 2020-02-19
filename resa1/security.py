from user import User 
from werkzeug.security import safe_str_cmp

usersDB = [
    User(1, 'user1', 'asdf'),
    User(2, 'user2', 'qwer')
]

username_map = {u.username : u for u in usersDB}
userid_map = {u.id : u for u in usersDB}


def authenticate(username, password):
    user  = username_map.get(username, None)
    if user and safe_str_cmp(user.password, password) :
        return user 
    

def identity(payload):
    user_id = payload["identity"]
    return userid_map.get(user_id, None)




