import pyautogui
import pyperclip
from time import sleep
import platform
import pandas as pd

'''
从 csv 表中读取要输入到 chatgpt 的查询文本，问题的提示模板在下面构造，支持多提示。
'''

template1 = '''
根据以下中医知识：
"{content}"
请你为我构造一个多轮问答数据，包含用户的问题和你认为的标准答案。格式为：
用户：[]。
回答：[]。'''
template2 = '''
根据以下中医知识：
"{content}"
从【名言出处】的角度出发，为我构造一个问答数据，包含一个用户的问题和一个标准答案格式为：
用户：[]。
回答：[]。'''

def read_csv_file(file_path):
    # 读取csv文件
    df = pd.read_csv(file_path)
    # 遍历“content”列中的所有元素
    for part in df['content']:
        if part.strip():  # 检查分段是否为空
            print(part)
            prompt1 = template1.replace('{content}', part)
            prompt2 = template2.replace('{content}', part)

            # 将 prompt1 和 prompt2 放入列表
            prompts = [prompt1, prompt2]

            # 循环执行复制和粘贴操作
            for prompt in prompts:
                pyperclip.copy(prompt + '\n')  # 复制文本到剪贴板

                # 判断当前操作系统是Windows还是Mac，然后执行相应的粘贴操作
                if platform.system() == 'Windows':
                    pyautogui.keyDown('ctrl')  # 按下 'ctrl' 键
                    pyautogui.press('v')  # 模拟 'v' 键，进行粘贴
                    pyautogui.keyUp('ctrl')  # 松开 'ctrl' 键
                elif platform.system() == 'Darwin':  # 'Darwin' 是 Mac OS X 的内核名称
                    pyautogui.keyDown('command')  # 按下 'command' 键
                    pyautogui.press('v')  # 模拟 'v' 键，进行粘贴
                    pyautogui.keyUp('command')  # 松开 'command' 键

                pyautogui.press('enter')  # 模拟 'enter' 键，发送文本
                sleep(10)  # 等待 10 秒

sleep(5)  # 延迟 5 秒执行，请 5 秒内打开活动窗！
# 读取文件
read_csv_file('data/problems.csv')
