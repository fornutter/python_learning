from flask import Flask, render_template
from bus_search import bus_search

app = Flask(__name__)

@app.route("/bus/<direction>")
def bus(direction):

    bus = bus_search()

    result = bus.direct_bus(direction)

    return render_template("index.html", result=result, direction=direction)


if __name__ == "__main__":
    app.run()
