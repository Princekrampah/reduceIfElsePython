from typing import Any, Dict


def _handle_addition(x, y):
    print(x + y)


def _handle_substraction(x, y):
    print(x - y)


def _handle_division(x, y):
    print(x/y)


def _handle_multiplication(x, y):
    print(x * y)


def action_handler(request: Dict[str, Any]):
    request_action = request.get("action")
    request_data = request.get("data")
    
    if request_action == "add":
        _handle_addition(request_data[0], request_data[1])
    
    elif request_action == "sub":
        _handle_substraction(request_data[0], request_data[1])

    elif request_action == "div":
        _handle_division(request_data[0], request_data[1])

    elif request_action == "mult":
        _handle_multiplication(request_data[0], request_data[1])



action1 = {
    "action": "mult",
    "data": [20, 40]
}


action_handler(action1)


# This code makes the time complexity to be O(n) due 
# to all the if and elif statements.