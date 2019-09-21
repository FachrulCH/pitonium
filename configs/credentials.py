from . import env

DEFAULT_LOGIN = env.get('DEFAULT_LOGIN', 'need_login_plz')
DEFAULT_PASSWORD = env.get('DEFAULT_PASSWORD', 'need_password_plz')

USERS = {
    'default' :{
        'login': DEFAULT_LOGIN,
        'password': DEFAULT_PASSWORD
    },
}

def get_user(user):
    _user = USERS.get(user)
    if not _user:
        raise ValueError('Undifined user {}'.format(user))
    return _user