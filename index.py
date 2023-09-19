from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Instantiate the default model outside the route
default_model_name = 'hkunlp/instructor-xl'
embedding_model = HuggingFaceInstructEmbeddings(model_name=default_model_name)

@app.route("/v1/embeddings", methods=['POST'])
def embeddings():
    global embedding_model
    data = request.json
    text_input = data.get('input')
    
    # Handle both string and list inputs
    if isinstance(text_input, list):
        concatenated_input = ' '.join(text_input)
    else:
        concatenated_input = text_input

    model_name = data.get('model', default_model_name)
    
    # If a different model is requested, instantiate a new model
    if model_name != default_model_name:
        embedding_model = HuggingFaceInstructEmbeddings(model_name=model_name)
    
    embeddings_list = embedding_model.embed_documents(concatenated_input)
    
    response_data = {
        "data": [{
            "embedding": embeddings_list[0],
            "index": 0,
            "object": "embedding"
        }],
        "model": model_name,
        "object": "list",
        "usage": {
            "prompt_tokens": len(concatenated_input.split()),
            "total_tokens": len(embeddings_list[0])
        }
    }
    
    if app.config['DEBUG']:
        response_data_copy = response_data.copy()
        response_data_copy['data'][0]['embedding'] = response_data_copy['data'][0]['embedding'][:5]
        print("Response Data:", response_data_copy)  # Print response data with only first 5 embeddings # Print response data

    return jsonify(response_data)

port_no = os.environ.get('PORT', 5000)

print(f"Server running on port {port_no}....")
app.run(host='0.0.0.0', port=int(port_no))
