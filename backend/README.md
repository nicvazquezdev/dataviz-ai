# Backend Configuration

## OpenAI API Key Setup

To use the full functionality of this application, you need to configure an OpenAI API key:

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a `.env` file in the backend directory
3. Add your API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Demo Mode

If no API key is configured or if the API key is invalid, the application will automatically switch to **Demo Mode** and show sample data based on your questions. You'll see a yellow warning banner indicating that demo data is being used.

## Features

- **Full Mode**: With valid API key - generates real SQL queries and executes them on your data
- **Demo Mode**: Without API key - shows realistic sample data based on your questions

## Running the Application

1. Install dependencies: `pip install -r requirements.txt`
2. Load data: `python load_data.py`
3. Start server: `uvicorn app.main:app --reload`

The application will work in both modes, providing a seamless experience regardless of API key configuration.
