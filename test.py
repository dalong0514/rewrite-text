import os, time
import openai
import json

from tqdm import tqdm

# get the api_key from config.json
def get_api_key():
    with open('../../config.json') as f:
        config = json.load(f)
    return config['API_KEY_1']

openai.api_key = get_api_key()

# 步骤一：读取文件并拆分字符串
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return content

# 生成内容
def generate_content(content, prompt):
    content = prompt + '\n{\n' + content + '}'
    completion = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "user", "content": content}
    ]
    )
    responsed_content = completion.choices[0].message.content + '\n'
    return responsed_content

# 步骤三：合并处理后的字符串并写入新文件
def write_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def progress_decorator(func):
    def wrapper(*args, **kwargs):
        total_steps = 2  # 假设函数有4个主要步骤
        with tqdm(total=total_steps, desc="Function progress") as pbar:
            return func(pbar, *args, **kwargs)
    return wrapper

@progress_decorator
def rewrite_text(pbar):
    # 第一步进度条
    time.sleep(0.1)
    pbar.update(1)

    # 获取当前文件夹的路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 定义源文件和目标文件的路径
    origin_path = os.path.join(current_directory, 'origin_text_1.md')
    target_path = os.path.join(current_directory, 'target_text_1.md')
    prompt_path = os.path.join(current_directory, 'prompt_text.md')

    # 读取源文件的内容并按字符拆分
    content = read_file(origin_path)

    prompt = read_file(prompt_path)
    processed_content = generate_content(content, prompt)
    write_file(processed_content, target_path)

    # 第二步进度条
    time.sleep(0.1)
    pbar.update(1)

if __name__ == '__main__':
    start_time = time.time()
    progress_decorator(rewrite_text())
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
