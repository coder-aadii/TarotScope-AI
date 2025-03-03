# TarotScope-AI: AI-Powered Tarot Reading

This project is the second phase of the **TarotScope** application, aiming to integrate an AI model that provides insightful and context-aware tarot card readings. This microservice is built using Python and serves as a backend service that processes user questions and selected tarot cards to generate detailed interpretations by leveraging Natural Language Processing (NLP) and AI-powered text generation.

---

## Project Structure

```
TarotScope-AI/
├─ app.py                # Flask server to handle requests
├─ utils.py              # Contains helper functions for NLP, tarot card meanings, and AI generation
├─ tarot_cards.json       # Stores tarot card data with names, arcana, and meanings
├─ venv/                 # Python virtual environment
├─ requirements.txt       # Dependencies for the project
└─ README.md             # Project description and setup guide
```

---

## Features

1. **NLP-Based Question Analysis**: Analyzes the user’s question to extract meaning, intent, and emotional context using NLP.
   
2. **Tarot Card Interpretation**: Fetches relevant upright or reversed meanings of the selected tarot cards from a data source.

3. **AI-Generated Reading**: Combines the user's question and tarot card meanings, then uses a pre-trained AI language model (GPT-2) to generate a descriptive, personalized reading.

4. **REST API Integration**: Exposes endpoints that allow the TarotScope front end to communicate with this service and retrieve generated tarot readings.

---

## Technologies Used

- **Python 3.9+**
- **Flask**: Lightweight web framework to serve the AI model as a REST API.
- **spaCy**: For Natural Language Processing (NLP) to analyze user questions.
- **Hugging Face Transformers**: For AI-powered text generation (GPT-2 model).
- **JSON**: For storing tarot card data with upright and reversed meanings.

---

## Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TarotScope-AI.git
cd TarotScope-AI
```

### 2. Create and Activate a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python app.py
```

The Flask server should now be running on `http://127.0.0.1:5000/`.

---

## API Endpoints

### 1. **Home Endpoint**

- **URL**: `/`
- **Method**: `GET`
- **Response**: Welcome message

```json
{
  "message": "Welcome to TarotScope AI!"
}
```

### 2. **Analyze Question Endpoint**

- **URL**: `/analyze`
- **Method**: `GET`
- **Response**: Returns tokens (words) extracted from the user’s question using NLP.

```json
{
  "tokens": ["What", "does", "my", "future", "hold", "?"]
}
```

### 3. **Generate Tarot Reading (Planned)**

- **URL**: `/generate-reading`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
    "question": "What does my future hold?",
    "cards": [
      {"name": "The Fool", "arcana": "Major Arcana", "position": "upright"},
      {"name": "The Magician", "arcana": "Major Arcana", "position": "reversed"},
      {"name": "The High Priestess", "arcana": "Major Arcana", "position": "upright"}
    ]
  }
  ```
- **Response**: Returns a detailed tarot reading combining the question and selected cards.

---

## Next Steps

- Implement the `/generate-reading` endpoint that combines user question analysis and tarot card meanings to generate a custom reading.
- Deploy the service on a free hosting platform like Heroku or Deta to integrate with the TarotScope front end.

---

## Contributing

If you’d like to contribute to the project, feel free to open a pull request or raise an issue.

---

## License

This project is open-source and available under the [MIT License](LICENSE).