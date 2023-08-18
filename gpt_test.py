import os, time
import openai

from tqdm import tqdm

def progress_decorator(func):
    def wrapper(*args, **kwargs):
        total_steps = 4  # 假设函数有4个主要步骤
        with tqdm(total=total_steps, desc="Function progress") as pbar:
            return func(pbar, *args, **kwargs)
    return wrapper

openai.api_key = "sk-" + "9YonsFAkxw09A3IDkL5qT3BlbkFJ8j80Aco5ecfDRJRYsbce"

@progress_decorator
def rewrite_text(pbar):
    # 第一步
    time.sleep(0.1)
    pbar.update(1)
    
    # 获取当前文件夹的路径
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 定义源文件和目标文件的路径
    origin_path = os.path.join(current_directory, 'origin_text.md')
    target_path = os.path.join(current_directory, 'target_text.md')

    # 读取源文件的内容
    with open(origin_path, 'r') as origin_file:
        content = origin_file.read()

    # 第二步
    time.sleep(0.1)
    pbar.update(1)

    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": content}
    ]
    )

    # 第三步
    time.sleep(0.1)
    pbar.update(1)

    # 将读取的内容写入目标文件
    with open(target_path, 'w') as target_file:
        target_file.write(completion.choices[0].message.content)

    # print(completion.choices[0].message.content)
    # 第四步
    time.sleep(0.1)
    pbar.update(1)

if __name__ == '__main__':
    start_time = time.time()
    rewrite_text()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
