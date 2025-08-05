import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ["API_KEY"])

sys_prompt = "You are a friendly and supportive teaching assistant for CS50."
user_prompt = input("What is your question? ")

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # ✅ Use this if you don't have GPT-4 access
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt},
    ]
)

response_content = chat_completion.choices[0].message.content
print(response_content)
