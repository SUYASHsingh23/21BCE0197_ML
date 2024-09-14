from flask import Flask, request, jsonify
from redis import Redis
from pymongo import MongoClient
import time

app = Flask(__name__)

# Connect to Redis (for caching) and MongoDB (for document storage)
redis_cache = Redis(host='localhost', port=6379)
client = MongoClient('mongodb://localhost:27017/')
db = client['doc_retrieval']
documents = db['documents']

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is up and running!"}), 200

@app.route('/search', methods=['POST'])
def search():
    start_time = time.time()

    data = request.get_json()
    text = data.get('text', '')
    top_k = data.get('top_k', 5)
    threshold = data.get('threshold', 0.5)
    user_id = data.get('user_id')

    # Check user rate limiting
    user_entry = redis_cache.get(user_id)
    if user_entry and int(user_entry) > 5:
        return jsonify({"error": "Rate limit exceeded"}), 429
    else:
        redis_cache.incr(user_id)
    
    # Placeholder search logic
    search_results = ["Document1", "Document2"]  # Simulated results
    elapsed_time = time.time() - start_time

    return jsonify({"results": search_results, "inference_time": elapsed_time}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
