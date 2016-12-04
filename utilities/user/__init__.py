#
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    from app.models import User
    return User.query.get(int(id))
#
