from .base import *

DEBUG = True

ALLOWED_HOSTS = []

#ロギングの設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,

    'formatters':{
        'dev':{
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
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev',
        },
    },

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
}

EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'
#これでメールの送信先がコンソールになる