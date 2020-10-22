from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate

bootstrap = Bootstrap()
ckeditor = CKEditor()
login_manager = LoginManager()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
csrf = CSRFProtect()
toolbar = DebugToolbarExtension()
migrate = Migrate()


def init_ext(app):
    bootstrap.init_app(app)
    ckeditor.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)


@login_manager.user_loader
def load_user(user_id):
    from mybluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"
