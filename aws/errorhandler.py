import logging
from flask_smorest import Blueprint
from werkzeug.exceptions import NotFound

logger = logging.getLogger(__name__)
blueprint = Blueprint("errorhandler", __name__)


def error_template(func):
    def wrapper(*args, **kwargs):
        body, status = func(*args, **kwargs)
        return {"status": status, **body}, status

    return wrapper


@blueprint.app_errorhandler(Exception)
@error_template
def handle_exception(error):
    logger.error(error)
    return {"message": "Unexpected error occured."}, 500


@blueprint.app_errorhandler(NotFound)
@error_template
def handle_not_found(error):
    logger.error(error)
    return {"message": "The requested URL was not found on the server."}, error.code
