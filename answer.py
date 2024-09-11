# main.py

from parser import get_text_from_url
from ask import ask_question

def ask_from_website(url, question):
    text = get_text_from_url(url)
    
    if text.startswith("An error occurred:"):
        return text
    
    prompt = f"The following text was extracted from {url}:\n\n{text}\n\nQuestion: {question}"

    answer = ask_question(prompt, text)
    
    return answer

# Example usage
url = "https://en.wikipedia.org/wiki/Vampeta"
question = "How old is he?"
print(ask_from_website(url, question))
