from flask import Flask, request, jsonify
from core.finder import VerseFinder

app = Flask(__name__)
app.json.ensure_ascii = False

finder = VerseFinder()


@app.route("/verses", methods=["GET"])
def get_verses():
    name = request.args.get("name", "").strip()
    book = request.args.get("book")

    if not name:
        return jsonify({"error": "missing name parameter"}), 400

    try:
        results = finder.find(name=name, book_name=book)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "count": len(results),
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)
