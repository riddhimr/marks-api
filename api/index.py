import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load JSON file
with open(os.path.join(os.path.dirname(__file__), '..', 'marks.json')) as f:
    marks = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    results = [marks.get(name, None) for name in names]
    return jsonify({"marks": results})

# Vercel Python adapter
def handler(environ, start_response):
    return app(environ, start_response)
