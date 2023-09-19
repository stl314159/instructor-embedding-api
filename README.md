# Instructor Embedding API

This API is designed to generate embeddings using models from the Hugging Face platform. By default, it uses the [hkunlp/instructor-xl](https://huggingface.co/hkunlp/instructor-xl) model to generate the embeddings.

## Compatibility

The API was implemented to provide basic compatibility with the [LocalAI project](https://github.com/go-skynet/LocalAI). This ensures that it can be easily used by LangChain:

```python
from langchain.embeddings import LocalAIEmbeddings
embeddings = LocalAIEmbeddings(openai_api_base="http://{SERVER_IP}:{SERVER_PORT}/v1", model="hkunlp/instructor-xl")
```

## Features

- **Default Model**: The API uses the [hkunlp/instructor-xl](https://huggingface.co/hkunlp/instructor-xl) model by default for generating embeddings.
  
- **Flexibility**: Although the default model is `hkunlp/instructor-xl`, the API is designed to be flexible. It should work with other Hugging Face embedding models, allowing users to switch to different models if needed.

## Getting Started

1. **Clone the Repository**: 

   ```bash
   git clone https://github.com/stl314159/instructor-embedding-api.git
   ```

2. **Configuration Setup**:

   Navigate to the project directory:

   ```bash
   cd instructor-embedding-api
   ```

   Copy the example environment configuration:

   ```bash
   cp .env-example .env
   ```

   Modify the `.env` file to suit your environment.

3. **Running the API with Docker**:

   Once the configuration is set, run the API using Docker Compose:

   ```bash
   docker-compose up
   ```

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss the proposed change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
