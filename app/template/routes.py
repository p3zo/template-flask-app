import flask

from template import logger


bp = flask.Blueprint("template", __name__)


def log_request_start(request):
    logger.info("---------- ---------- ---------- ----------")
    logger.info(request.url)
    logger.info("\n")


def mk_error_response(msg, status_code):
    message = {
        "status": status_code,
        "message": msg,
    }
    response = flask.jsonify(message)
    response.status_code = status_code
    response.headers.add("Access-Control-Allow-Origin", "*")

    logger.info(f"Serving error response with message `{msg}`: {response}")

    return response


def mk_response(body, status_code):
    response = flask.jsonify(body)
    response.status_code = status_code
    response.headers.add("Access-Control-Allow-Origin", "*")

    logger.info(f"Serving response: {response}")

    return response


@bp.route("/", methods=["GET"])
def index():
    log_request_start(flask.request)

    response_body = {"index": "hello"}

    return mk_response(response_body, 200)
