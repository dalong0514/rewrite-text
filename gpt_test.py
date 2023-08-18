import os, time
import openai

openai.api_key = "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"

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