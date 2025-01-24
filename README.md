
# ChatGPT Connector API

A robust Chatbot API powered by OpenAI's ChatGPT.

## Features

- **Endpoints**:
  - `/health`: Health check endpoint.
  - `/chat`: POST endpoint for chatbot interaction.
- **Authentication**: API key-based authentication.
- **Environment Variables**: Manage sensitive data via `.env` file.
- **Docker Support**: Easily containerize the API.

## Setup

1. Clone the repository and navigate to the project directory.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on `.env.example` and fill in your OpenAI API key and valid API keys.
4. Run the API:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

5. Optionally, use Docker:

   ```bash
   docker build -t chatgpt-connector-api .
   docker run -p 8000:8000 chatgpt-connector-api
   ```

## Environment Variables

The following variables need to be set in a `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `VALID_API_KEYS`: Comma-separated list of valid API keys for authentication.

## License

This project is licensed under the MIT License.
