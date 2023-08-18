import os, time
import openai

openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)


# if __name__ == '__main__':
#     start_time = time.time()
#     test_gpt()
#     end_time = time.time()
#     print('OK!')
#     print('Time Used: ' + str(end_time - start_time) + 's')