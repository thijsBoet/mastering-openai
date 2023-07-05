import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a friendly game show host."},
#         {"role": "user", "content": "generate three trivia questions and answers"}
#     ]
# )

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant that classifies sentiment as either positive, neutral or negative."},
#         {"role": "user", "content": "classify the sentiment in the following text: I like pizza"},
#         {"role": "assistant", "content": "Positive"},
#         {"role": "user", "content": "classify the sentiment in the following text: I don't like chickens"},
#     ]
# )

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.7,
    top_p=1.0,
    max_tokens=500,
    messages=[
        {"role": "system", "content": "You are a helpful dutch assistant that writes sinterklaas rhymes"},
        {"role": "user", "content": "Schrijf een leuk grappig Sinterklaasgedicht over antiek, schilderijen en antiekveilingen"},
    ]
)

print(response.choices[0].message.content)