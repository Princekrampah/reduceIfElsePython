from typing import Any, Dict


def _handle_addition(x, y):
    print(x + y)


def _handle_substraction(x, y):
    print(x - y)


def _handle_division(x, y):
    print(x/y)


def _handle_multiplication(x, y):
    print(x * y)


MAPPER = {
    "add": _handle_addition,
    "sub": _handle_substraction,
    "div": _handle_division,
    "mult": _handle_multiplication
}

def action_handler(request: Dict[str, Any]):
    request_action = request.get("action")
    request_data = request.get("data")
    request_handler(request_action, request_data)


def request_handler(request_action, request_data):
    handler_function = MAPPER.get(request_action)
    handler_function(request_data[0], request_data[1])


action1 = {
    "action": "mult",
    "data": [20, 40]
}

action_handler(action1)

