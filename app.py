import os
from flask import Flask, jsonify, request
import nltk
from language_tool_python import LanguageTool
from nltk.tokenize import sent_tokenize
from flask_cors import CORS  # Import CORS

# Define the project directory and NLTK data directory
project_dir = os.path.dirname(os.path.abspath(__file__))
nltk_data_dir = os.path.join(project_dir, 'nltk_data')

# Create the NLTK data directory if it doesn't exist
os.makedirs(nltk_data_dir, exist_ok=True)
os.environ['NLTK_DATA'] = nltk_data_dir

# Download NLTK data
nltk.download('words', download_dir=nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}) # Initialize CORS


# Route to get all items
@app.route('/', methods=['GET'])
def get_items():
    print("hello")
    return jsonify({"id": 1, "name": "Item 1"})

@app.route('/yourname', methods=['GET'])
def get_name():
    print("hello")
    return "Nitin Singh"

# Route to create a new item
@app.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    print(data)
    
    grammerMistakes = check_grammar_with_languagetool(data['summary'])
    
    extracted_mistakes = []

    for mistake in grammerMistakes:
        extracted_mistake = {
            'error': mistake.matchedText, 
            'replacements': mistake.replacements,
            'context':mistake.context,
        }
        extracted_mistakes.append(extracted_mistake)
    
    
    mistakes = {
        'grammerMistakes': extracted_mistakes
    }
    
    
    finalData = jsonify(mistakes)
    print(finalData)
    return finalData, 201


def check_grammar_with_languagetool(text):
    mistakes = []
    tool = LanguageTool('en-US')
    sentences = sent_tokenize(text)
    for sentence in sentences:
        matches = tool.check(sentence)
        for match in matches:
            mistakes.append(match)
    return mistakes  

if __name__ == '__main__':
    app.run(port=1234,debug=True)




