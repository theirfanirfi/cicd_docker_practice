from flask import Flask, render_template, request

from calculator import OPERATIONS, OperationNotSupported, calculate

app = Flask(__name__)


def _parse_number(raw, label):
    if raw is None or raw.strip() == "":
        raise ValueError("%s is required." % label)
    try:
        return float(raw)
    except ValueError:
        raise ValueError("%s must be a number." % label)


def _format(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


@app.route("/", methods=["GET", "POST"])
def index():
    a_raw = request.form.get("a", "")
    b_raw = request.form.get("b", "")
    operation = request.form.get("operation", "add")
    result = None
    expression = None
    error = None

    if request.method == "POST":
        try:
            a = _parse_number(a_raw, "First number")
            b = _parse_number(b_raw, "Second number")
            symbol, value = calculate(operation, a, b)
            result = _format(value)
            expression = "%s %s %s" % (_format(a), symbol, _format(b))
        except (ValueError, OperationNotSupported) as exc:
            error = str(exc)

    return render_template(
        "index.html",
        operations=OPERATIONS,
        a=a_raw,
        b=b_raw,
        operation=operation,
        result=result,
        expression=expression,
        error=error,
    )


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
