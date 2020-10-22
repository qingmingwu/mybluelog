import os
import uuid

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# DEBUG = True
# SECRET_KEY = "secret_key"
# SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
# SQLALCHEMY_TRACK_MODIFICATIONS = False

class BaseConfig(object):
    # SECRET_KEY = os.getenv("SECRET_KEY", "dev key")
    SECRET_KEY = uuid.uuid4().hex
    DEBUG_TB_INTERCEPT = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = "admin.upload_image"

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("Bluelog Admin", MAIL_USERNAME)

    BLUELOG_EMAIL = os.getenv("BLUELOG_EMAIL")
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15

    BLUELOG_THEMES = {"perfect_blue": "Perfect Blue", "black_swan": "Black Swan"}
    BLUELOG_SLOW_QUERY_THRESHOLD = 1

    BLUELOG_UPLOAD_PATH = os.path.join(basedir, "uploads")
    BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]

    # debugtoolbar 允许重定向
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = "redis"

    # SSL_DISABLED = True


class DevelopmentConfig(BaseConfig):
    # print("111111111111111111111111111111111111111111111", os.getenv("SQLALCHEMY_DATABASE_URI"))
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI").format("mybluelog")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI1")


class TestingConfig(BaseConfig):
    # print("222222222222222222222222222222222222222222222", os.getenv("SQLALCHEMY_DATABASE_URI"))
    TESTING = True
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI").format("testingmybluelog")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     "SQLALCHEMY_DATABASE_URI2") or "mysql+pymysql://root:585756@localhost:3306/testingmybluelog?charset=utf8"


class ProductionConfig(BaseConfig):
    # SSL_DISABLED = False
    # print("333333333333333333333333333333333333333333333", os.getenv("SQLALCHEMY_DATABASE_URI"))
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI").format("testingmybluelog")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI3")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
