"""Exercise 2: Unit converter (starter): the web page.

A page with a number box, a "from" menu and a "to" menu. Submitting shows the
result under the form. A non-number, or incompatible units, shows a friendly error.

Tip: read the number in its own try block, SEPARATE from the call to convert().
Two different problems raise ValueError, and keeping them apart lets each show
the right message. Write templates/convert.html yourself.
"""

from flask import Flask, render_template, request

from converter import UNITS, convert

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    # TODO
    return "Converter coming soon"


if __name__ == "__main__":
    app.run(debug=True)
