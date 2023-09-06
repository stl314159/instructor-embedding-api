from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings

from flask import Flask, request
from flask_cors import CORS

import os

# Load the embedding model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET', 'POST'])
def embeddings():
  if request.method == 'GET':
    docs = request.args.get('docs')
    return instructor_embeddings.embed_documents(docs)

  elif request.method == 'POST':
    docs = request.json['docs']
    return instructor_embeddings.embed_documents(docs)


port_no = os.environ.get('PORT', 5000)

print(f"Server running on port {port_no}....")
app.run(host='0.0.0.0', port=int(port_no))