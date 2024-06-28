from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['SNAIL']
collection = db['magic']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/save-message', methods=['POST'])
def save_message():
    data = request.json
    magical_word = data.get('magicalWord')
    message = data.get('message')

    result = collection.update_one(
        {'magicalWord': magical_word},
        {'$set': {'message': message}},
        upsert=True
    )

    if result.modified_count > 0 or result.upserted_id:
        return jsonify({'message': 'Message saved successfully'}), 200
    else:
        return jsonify({'message': 'Failed to save message'}), 500

if __name__ == '__main__':
    app.run(debug=True)
