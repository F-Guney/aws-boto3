from flask import Flask
from flask_smorest import Api

from aws import config
from aws.errorhandler import blueprint as errorhandler_blueprint
from aws.ec2.route import blueprint as ec2_blueprint
from aws.ec2.power.route import blueprint as ec2_power_blueprint
from aws.s3.route import blueprint as s3_blueprint
from aws.s3.bucket.route import blueprint as s3_bucket_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    register_config(app)
    register_blueprints(app)
    return app


def register_config(app: Flask):
    config.init_app(app)


def register_blueprints(app: Flask):
    api = Api(app)
    api.register_blueprint(errorhandler_blueprint)
    api.register_blueprint(ec2_blueprint)
    api.register_blueprint(ec2_power_blueprint)
    api.register_blueprint(s3_blueprint)
    api.register_blueprint(s3_bucket_blueprint)


app = create_app()

if __name__ == "__main__":
    app.run()
