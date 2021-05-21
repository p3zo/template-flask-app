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


def mk_success_response(body, msg):
    message = {
        "status": 200,
        "body": body,
        "message": msg,
    }
    response = flask.jsonify(message)
    response.status_code = 200
    response.headers.add("Access-Control-Allow-Origin", "*")

    logger.info(f"Serving success response: {response}")

    return response


@bp.route("/extract", methods=["GET"])
def index():
    log_request_start(flask.request)

    response_body = {"index": "hello"}

    response = flask.jsonify(response_body)
    response.headers.add("Access-Control-Allow-Origin", "*")
    logger.info(f"Serving response: {response}")
    return response
