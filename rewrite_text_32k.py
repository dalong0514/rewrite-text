import os, time
import openai

from tqdm import tqdm

openai.api_key = "sk-" + "9YonsFAkxw09A3IDkL5qT3BlbkFJ8j80Aco5ecfDRJRYsbce"

# 步骤一：读取文件并拆分字符串
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return content


# 步骤一：读取文件并拆分字符串
def read_and_split_file(filename):
    content = read_file(filename)
    
    chunks = []
    chunk = ""
    
    for i in range(0, len(content), 1000):
        chunk = content[i:i+1000]
        chunks.append(chunk)
        
    return chunks


# 生成内容
def generate_content(content):
    completion = openai.ChatCompletion.create(
    model="gpt-4-32k",
    messages=[
        {"role": "user", "content": content}
    ]
    )
    responsed_content = completion.choices[0].message.content + '\n'
    return responsed_content


# 步骤二：处理内容
def process_chunks(chunks, prompt):
    modified_chunk = prompt + '\n{\n' + chunks + '}'
    responsed_content = generate_content(modified_chunk)
    return responsed_content

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

    # 读取源文件的内容
    content = read_file(origin_path)
    # 读取提示词
    prompt = read_file(prompt_path)
    processed_chunks = process_chunks(content, prompt)
    # 写入结果
    with open(target_path, 'w', encoding='utf-8') as file:
        file.write(processed_chunks)

    # 第二步进度条
    time.sleep(0.1)
    pbar.update(1)


if __name__ == '__main__':
    start_time = time.time()
    rewrite_text()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
