# Textro: Gemini Chatbot

A small web chatbot that answers questions using Google's Gemini model. It has a custom chat page with an animated mascot, and a Flask backend that passes each question to Gemini through LangChain and returns the answer.

## What it does

- **Answers any question.** Type a prompt on the page and get a response from Google Gemini 2.0 Flash.
- **Web chat interface.** A responsive single-page UI with a mascot, a prompt box and a scrollable answer panel.
- **REST endpoint.** The backend exposes a `POST /ask` endpoint that takes a JSON prompt and returns the model's response, so the same backend could serve other front ends.
- **Safe configuration.** The API key is read from environment variables and kept out of the code.

## Keywords

Generative AI · LLM · Chatbot · Google Gemini · LangChain · Flask · REST API · Prompt Engineering · Python · HTML · CSS · JavaScript

## Tech Stack

- Python
- [Flask](https://flask.palletsprojects.com/) for the web server and REST API
- [LangChain](https://www.langchain.com/) with `langchain-google-genai`
- [Google Gemini 2.0 Flash](https://ai.google.dev/) as the language model
- HTML, CSS and JavaScript for the front end
- python-dotenv for configuration

## Project Structure

| File | Purpose |
| :--- | :--- |
| `Text to Text Ai Model/app.py` | Flask backend: serves the page and the `/ask` endpoint |
| `Text to Text Ai Model/index.html` | Chat interface (HTML, CSS and JavaScript) |
| `Text to Text Ai Model/bot.png` | Chatbot mascot image |

## Author

**Amar Chaurasiya**, Data Scientist working as an AI Engineer.

- Email: [amarchaurasiya124@gmail.com](mailto:amarchaurasiya124@gmail.com)
- LinkedIn: [linkedin.com/in/amar-chaurasiya-163788262](https://www.linkedin.com/in/amar-chaurasiya-163788262)
- Portfolio: [amarchaurasiya.vercel.app](https://amarchaurasiya.vercel.app)
