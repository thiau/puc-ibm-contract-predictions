from app import app, jsonify, add_number


@app.route('/', methods=["GET"])
def hello():
    value = add_number(1, 1)
    return jsonify(status=200, response="Hello!", value=value)