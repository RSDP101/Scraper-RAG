from flask import Flask, render_template, request, jsonify
from parser import get_text_from_url  # Ensure parser.py and ask.py are accessible and properly set up
from ask import ask_question

app = Flask(__name__)

def ask_from_website(url, question):
    text = get_text_from_url(url)
    
    if text.startswith("An error occurred:"):
        return text
    
    prompt = f"The following text was extracted from {url}:\n\n{text}\n\nQuestion: {question}"

    answer = ask_question(prompt, text)
    
    return answer

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    url = request.json.get('url')
    question = request.json.get('question')
    
    if not url or not question:
        return jsonify({"error": "Both URL and question are required."})
    
    try:
        answer = ask_from_website(url, question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
