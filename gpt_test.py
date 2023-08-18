import os, time
import openai

# openai.api_key = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
# messages = [ {"role": "system", "content":
# 			"You are a intelligent assistant."} ]
# while True:
# 	message = input("User : ")
# 	if message:
# 		messages.append(
# 			{"role": "user", "content": message},
# 		)
# 		chat = openai.ChatCompletion.create(
# 			model="gpt-3.5-turbo", messages=messages
# 		)
# 	reply = chat.choices[0].message.content
# 	print(f"ChatGPT: {reply}")
# 	messages.append({"role": "assistant", "content": reply})

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "daglas0514@gmail.com", "content": "请介绍道金斯《自私的基因》的主要内容"}
  ]
)

print(completion.choices[0].message.content)


# if __name__ == '__main__':
#     start_time = time.time()
#     test_gpt()
#     end_time = time.time()
#     print('OK!')
#     print('Time Used: ' + str(end_time - start_time) + 's')