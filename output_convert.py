import csv

def convert_txt_to_csv(txt_file, csv_file):
    data = []

    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("用户："):
            user_question = line[4:]
            answer = lines[lines.index(line) + 1][4:]
            data.append({"Question": user_question, "Answer": answer})

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Question", "Answer"])
        writer.writeheader()
        writer.writerows(data)

    print(f"转换完成，已将文本文件 {txt_file} 转换为 CSV 文件 {csv_file}。")

# 示例使用方式
txt_file = 'input.txt'  # 输入的文本文件路径
csv_file = 'output.csv'  # 输出的 CSV 文件路径

convert_txt_to_csv(txt_file, csv_file)
