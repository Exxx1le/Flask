from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users',static_folder='../static')

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Ed'
}

# при обращении к адресу localhost/users/ будет срабатывать функция ниже
@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS
        )


@user.route('/<int:pk>')
def get_user(pk: int):
    user_name = USERS[pk]
    return render_template(
        'users/details.html',
        users=user_name
    )