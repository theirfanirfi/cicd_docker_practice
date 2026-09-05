"""Arithmetic operations for the calculator app.

Only addition is implemented; the remaining operations are intentional
placeholders that raise NotImplementedError.
"""


class OperationNotSupported(Exception):
    """Raised when an operation exists in the UI but is not implemented yet."""


def add(a, b):
    return a + b


def subtract(a, b):
    raise OperationNotSupported("Subtraction is not implemented yet.")


def multiply(a, b):
    raise OperationNotSupported("Multiplication is not implemented yet.")


def divide(a, b):
    raise OperationNotSupported("Division is not implemented yet.")


OPERATIONS = {
    "add": ("+", add),
    "subtract": ("-", subtract),
    "multiply": ("x", multiply),
    "divide": ("/", divide),
}


def calculate(operation, a, b):
    """Run `operation` on two numbers, returning (symbol, result)."""
    if operation not in OPERATIONS:
        raise OperationNotSupported("Unknown operation: %s" % operation)
    symbol, func = OPERATIONS[operation]
    return symbol, func(a, b)
