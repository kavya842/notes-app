from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import uuid, datetime

app = Flask(__name__)
CORS(app)

notes = []

def find_note(note_id):
    return next((n for n in notes if n['id'] == note_id), None)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    q = request.args.get('q', '').lower().strip()
    result = [n for n in notes if q in n['title'].lower() or q in n['body'].lower()] if q else notes
    return jsonify(result)

@app.route('/api/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    note = find_note(note_id)
    return jsonify(note) if note else (jsonify({'error': 'Not found'}), 404)

@app.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title required'}), 400
    note = {
        'id': str(uuid.uuid4()),
        'title': data['title'].strip(),
        'body': data.get('body', '').strip(),
        'created_at': datetime.datetime.now().isoformat(),
        'updated_at': datetime.datetime.now().isoformat()
    }
    notes.append(note)
    return jsonify(note), 201

@app.route('/api/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    note = find_note(note_id)
    if not note:
        return jsonify({'error': 'Not found'}), 404
    data = request.get_json()
    if 'title' in data: note['title'] = data['title'].strip()
    if 'body' in data: note['body'] = data['body'].strip()
    note['updated_at'] = datetime.datetime.now().isoformat()
    return jsonify(note)

@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    note = find_note(note_id)
    if not note:
        return jsonify({'error': 'Not found'}), 404
    notes = [n for n in notes if n['id'] != note_id]
    return jsonify({'message': 'Deleted'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)