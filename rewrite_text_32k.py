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
    # 按换行符分割文本
    lines = content.split('。')
    
    chunks = []
    chunk = ""
    
    for line in lines:
        # 检查新的行加入chunk后是否超过1000字符
        if len(chunk) + len(line) + 1 <= 1000:  # 加1是为了计算换行符
            chunk += line + '。'
        else:
            chunks.append(chunk)
            chunk = line + '。'
    
    # 添加最后一个块
    if chunk:
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
    processed_chunks = []
    for chunk in chunks:
        modified_chunk = prompt + '\n{\n' + chunk + '}'
        responsed_content = generate_content(modified_chunk)
        processed_chunks.append(responsed_content)
    return processed_chunks


# 步骤三：合并处理后的字符串并写入新文件
def merge_and_save_chunks(chunks, filename):
    merged_text = ''.join(chunks)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(merged_text)


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
    chunks = read_and_split_file(origin_path)

    prompt = read_file(prompt_path)
    processed_chunks = process_chunks(chunks, prompt)
    merge_and_save_chunks(processed_chunks, target_path)

    # 第二步进度条
    time.sleep(0.1)
    pbar.update(1)


if __name__ == '__main__':
    start_time = time.time()
    rewrite_text()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
