from flask import jsonify, request

from ..utils.logger import log_action
from .jwt_handler import decode_jwt


def check_jwt():
    # Gets token from request header and tries to get it's payload
    # Will raise errors if token is missing, invalid or expired
    token = request.headers.get("Authorization")
    if not token:
        raise Exception("Missing access token")
    jwt = token.split("Bearer ")[1]
    try:
        return decode_jwt(jwt)
    except Exception as e:
        raise Exception(f"Invalid access token: {e}") from e


def auth_guard(role=None):
    def wrapper(route_function):
        def decorated_function(*args, **kwargs):
            # Authentication gate
            try:
                user_data = check_jwt()
            except Exception as e:
                log_action(__name__, str(e), route_function.__name__, "", "", "warning")

                return jsonify({"message": f"{e}", "status": 401}), 401

            # Authorization gate
            if role and role not in user_data["roles"]:
                log_action(
                    __name__,
                    "Invalid Role Authorization required",
                    route_function.__name__,
                    "",
                    "",
                    "warning",
                )
                return (
                    jsonify(
                        {
                            "message": "Invalid Role Authorization required ",
                            "status": 403,
                        }
                    ),
                    403,
                )
            # Proceed to original route function
            return route_function(*args, **kwargs)

        decorated_function.__name__ = route_function.__name__
        return decorated_function

    return wrapper
