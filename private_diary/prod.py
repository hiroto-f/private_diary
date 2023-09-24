from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
EMAIL_BACKEND = 'django_ses.SESBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,

    'formatters':{
        'prod':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    },

    'handlers':{
        'console':{
            'level':'INFO',
            'class':'logging.TimedRotatingFileHandler',
            'filename':os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter':'prod',
            'when':'D',
            'interval':1,
            'backupCount':7,
        },
    },

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'diary':{
            'handlers':['console'],
            'level':'INFO',
        },
    },
}
