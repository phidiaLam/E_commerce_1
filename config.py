'''
Autor: Wentao Lin
Description: the config of application
Date: 2020-12-26 12:17:46
LastEditTime: 2020-12-30 21:45:50
LastEditors: Wentao Lin
'''
import logging.config
import os
import app

WTF_CSRF_ENABLED = False
SECRET_KEY = '1BCDEFGHIJKLMNOPQRSTUVWXYZ12345'


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db?check_same_thread=False')
SQLALCHEMY_TRACK_MODIFICATIONS = True



logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            },
            "debug_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "debug.log",
                "maxBytes": 10485760,
                "backupCount": 50,
                "encoding": "utf8",
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "simple",
                "filename": "errors.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8",
            },
        },
        "loggers": {
            "my_module": {"level": "ERROR", "handlers": ["console"], "propagate": "no"}
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["error_file_handler", "debug_file_handler"],
        },
    }
)
