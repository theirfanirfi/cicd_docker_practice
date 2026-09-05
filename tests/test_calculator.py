import pytest

from app import app
from calculator import OperationNotSupported, add, calculate


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_add():
    assert add(2, 3) == 5
    assert add(-1.5, 0.5) == -1.0


@pytest.mark.parametrize("operation", ["subtract", "multiply", "divide"])
def test_other_operations_not_implemented(operation):
    with pytest.raises(OperationNotSupported):
        calculate(operation, 4, 2)


def test_index_renders(client):
    assert client.get("/").status_code == 200


def test_addition_via_form(client):
    res = client.post("/", data={"a": "2", "b": "3", "operation": "add"})
    assert b"2 + 3 =" in res.data
    assert b">5<" in res.data or b"= 5" in res.data or b"5" in res.data


def test_unimplemented_op_shows_error(client):
    res = client.post("/", data={"a": "4", "b": "2", "operation": "divide"})
    assert b"not implemented yet" in res.data


def test_invalid_input_shows_error(client):
    res = client.post("/", data={"a": "abc", "b": "3", "operation": "add"})
    assert b"must be a number" in res.data


def test_healthz(client):
    assert client.get("/healthz").get_json() == {"status": "ok"}
