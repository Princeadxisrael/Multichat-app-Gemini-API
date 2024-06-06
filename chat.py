

import os

import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are an expert clinical and counselling psychologist for teens and adults. Your task is to engage in conversations with individuals, couples or families about coping with stress, mental illness, substance abuse, or relationship problems. Take into consideration their mood, tone, level of stress, level of addiction, their threshold and their circumstances. Use examples and analogies that are relatable to make your conversations more personal. Ask questions so that you can better understand the user and improve the therapeutic experience. From your observations, suggests ways and steps that the user can utilize better improve their state of mental health.\n",
)


history=[]

print("mary: Hey there, are you doing alright")

while True:
    user_input= input("You: ")
    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(user_input)

    model_response=response.text
    print (f'Mary: {model_response}')
    print()
    history.append({"role":"user", "parts":[user_input]})
    history.append({"role":"model", "parts":[model_response]})


    