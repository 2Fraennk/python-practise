#!/usr/bin/env python3

import openai

openai.api_key = str(open("api_key", "r").readline())

# create and check connection
# list models
models = openai.Model.list()
# print the first model's id
print(models.data[0].id)

# set some variables
text_input = "Good evening"
model_id = "gpt-3.5-turbo"
messages = [{"role": "user", "content": text_input}]
temperature = 0.8

# chat and get response
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=temperature)
response_message = response["choices"][0]["message"]

# keep up conversation
messages.append(response_message)

text_input = input("Give me your question: ")
messages.append(
    {
        "role": "user",
        "content": text_input
    }
)

# get next response
response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=temperature)
print(response2["choices"][0]["message"]["content"])
