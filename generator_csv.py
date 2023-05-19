import pyautogui
import pyperclip
from time import sleep
import platform

'''
从 csv 表中直接读取要输入到 chatgpt 的问题
'''

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 按 "{ " 划分
        parts = content.split("{")
        for part in parts:
            part = part.replace('}', '')
            if part.strip():  # 检查分段是否为空
                print(part)
                pyperclip.copy(part + '\n')  # 复制文本到剪贴板

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
                sleep(3)  # 等待3秒

# 延迟 10 秒，请 5 秒内打开活动窗！
sleep(10)
# 读取文件
read_txt_file('data/problems.csv')
