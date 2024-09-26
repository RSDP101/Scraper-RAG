from flask import Flask, render_template, request, jsonify
from parser import get_text_from_url  # Ensure parser.py and ask.py are accessible and properly set up
from ask import ask_question
from jaccard import optimal_text
app = Flask(__name__)

def ask_from_website(url, question):
    text = get_text_from_url(url)
    # print (f"current text: {text}")
    text2 = optimal_text(url, question)
    print (f"desired text : {text2}")

    if text.startswith("An error occurred:"):
        return text
    
    prompt = f"Consider the following question : {question}. Answer based on your knowledge and the following reference text:{text2}"
    # print (f"current prompt: {prompt}")
    answer = ask_question(prompt, text2)
    
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