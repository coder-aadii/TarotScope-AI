from transformers import GPT2Tokenizer, GPT2LMHeadModel
import random
import json
from flask import Flask, request, jsonify
import spacy
import torch

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Load tarot card data from JSON file
with open('data/tarot_cards.json', 'r') as file:
    tarot_data = json.load(file)

# Load the fine-tuned GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./fine_tuned_gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('./fine_tuned_gpt2')

# Ensure the model is set to evaluation mode
model.eval()

# Route to analyze the question, select tarot cards, and generate descriptive reading
@app.route('/analyze', methods=['POST'])
def analyze_question():
    data = request.get_json()
    question = data.get('question', '')

    # Process the question using spaCy
    doc = nlp(question)
    tokens = [{'text': token.text, 'lemma': token.lemma_, 'pos': token.pos_} for token in doc]

    # Pick 3 random tarot cards
    cards = random.sample(tarot_data, 3)

    # Prepare card info and meaning hints for paragraph generation
    card_info = []
    hint_text = ''
    for card in cards:
        upright = random.choice([True, False])  # Randomly determine if card is upright or reversed
        meaning = card['meanings']['upright'] if upright else card['meanings']['reversed']
        card_info.append({
            'name': card['name'],
            'arcana': card['arcana'],
            'meaning': meaning,
            'orientation': 'upright' if upright else 'reversed'
        })
        # Collect hints from each card's meaning for the final paragraph
        hint_text += f"{card['name']} ({'Upright' if upright else 'Reversed'}) - General: {meaning['general']}, Love: {meaning['love']}, Career: {meaning['career']}, Finance: {meaning['finance']}. "

    # Combine the question and card hints
    input_text = f"Question: {question}. The following cards were drawn: {hint_text}"

    # Tokenize the input for GPT-2
    inputs = tokenizer.encode(input_text, return_tensors='pt')

    # Generate a tarot reading using the fine-tuned GPT-2 model
    with torch.no_grad():
        outputs = model.generate(inputs, max_new_tokens=150, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the generated text
    generated_paragraph = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Format the response to include only the question, 3 random cards, and the generated meaningful paragraph
    return jsonify({
        'question': question,
        'cards': card_info,
        'reading': generated_paragraph
    })

if __name__ == '__main__':
    app.run(debug=True)
