# Free-Self-Instruct

## Intruduction
[self-instruct](https://github.com/yizhongw/self-instruct) 技术是指基于目前已经成熟的语言大模型来快速构造指令数据集（例如 ChatGPT）。self-instruct 之前的做法一般是基于 OpenAI 提供的 GPT API 接口来进行实现。然而这种做法费用高昂，且由于 Open 与国内糟糕的互联网环境导致访问速度极其缓慢。

我们这一项目旨在帮助大家**免费实现 self-instruct 指令构建**， 在本机就可以实现批量向例如 ChatGPT 这样的模型网页端发送对话。换句话说，我们实现了批量向 ChatGPT 提问，只需要提前设置好文本与模板即可。
此外，我们还提供了一些导出对话的快速方案。

##  Usage

我们提供了两种方案来实现

1. `generator_csv.py `
    直接在表格中编辑好问题与文本
2. `generator_csv.py`
   表格中指定要输入的文本，修改对应的提示模板即可
   
运行以上任意 python 脚本后，5 秒内快速点击聊天软件的对话窗口，就可以自动询问了。

目前暂不支持自动调整休眠时间，需要根据用户的提问长度来调整休眠时间！

对于问答数据导出，首先安装一个将会话记录转为 markdown 的插件，例如：
![img.png](img%2Fimg.png)

然后运行 `output_convert.py` 即可获取到 csv 格式的对话记录。

## 运行实例

![ScreenFlow.gif](img%2FScreenFlow.gif)

## 原理

pyautogui 是通过模拟键盘和鼠标输入来工作的，所以在脚本运行期间，你的电脑不能进行其他的键盘和鼠标操作，否则可能会影响脚本的运行。

## 提示

- 该方法不仅支持 ChatGPT，对于任何类 ChatGPT 产品，包括但不限于文心一言、阿里千问、讯飞星火均可使用。虽然如果用的次数太多可能有限制，把全文所有的类 ChatGPT 软件用一个遍，足以生成非常庞大的数据了。
- 该程序运行时要求不能操作电脑
