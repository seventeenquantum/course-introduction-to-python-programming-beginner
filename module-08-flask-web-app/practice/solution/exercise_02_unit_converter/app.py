from flask import Flask, render_template, request

from converter import UNITS, convert

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        try:
            value = float(request.form.get("value", ""))
        except ValueError:
            error = "Please enter a number."
        else:
            from_unit = request.form.get("from_unit", "")
            to_unit = request.form.get("to_unit", "")
            try:
                answer = convert(value, from_unit, to_unit)
            except ValueError as exc:
                error = str(exc)
            else:
                result = f"{value:g} {from_unit} = {answer:.2f} {to_unit}"
    return render_template("convert.html", units=UNITS, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
