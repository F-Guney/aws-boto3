import logging

from os import getenv
from flask import Flask


class Config:
    API_TITLE = "aws-boto3"
    API_VERSION = "0.0.1"
    OPENAPI_VERSION = "3.0.2"


class DevelopmentConfig(Config):
    LOGGING_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    LOGGING_LEVEL = logging.ERROR


def init_app(app: Flask):
    env = getenv("FLASK_ENV", "dev")
    config = {
        "dev": DevelopmentConfig,
        "prod": ProductionConfig,
    }[env]

    app.config.from_object(config)
