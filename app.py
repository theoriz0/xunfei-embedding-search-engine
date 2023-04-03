from search import search_subfeature
from flask import Flask, request, jsonify
from flask_api import status

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search_engine():
    search_result = search_subfeature(request.args.get('description'))
    return jsonify(search_result), status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)