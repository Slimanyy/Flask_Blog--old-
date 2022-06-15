import os


class Config:
    SECRET_KEY = "d812d31ee2758d676e1f579a4c1583b7"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('mail')
    MAIL_PASSWORD = os.environ.get('mailpass')