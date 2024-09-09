from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv('API_KEY')

client = OpenAI(
    # This is the default and can be omitted
	api_key = openai_key
)

def ask_question(prompt):
    MODEL = "gpt-4o"

    system_prompt = '''
    Add text here
    '''
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt },
            {"role": "user", "content": system_prompt + "\n" + prompt}
        ]
    )
    output = completion.choices[0].message.content
    return output


print(ask_question("according to text, what is the best country in the world?"))
