import deepl
import re
import os
import json

# JSON 파일 불러오기
with open("config.json", "r") as f:
    config = json.load(f)

# API 토큰 사용하기
api_token = config["auth_key"]

# 올바른 변수명으로 수정
translator = deepl.Translator(api_token)
print(os.getcwd())

# message를 text.txt에서 읽어와서 번역
with open("input.txt", "r", encoding="utf-8") as f:
    message = f.read()
    result = translator.translate_text(message, target_lang="KO")

# 파일이 없으면 새로 생성
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result.text)

# 파일을 읽는 부분은 그대로 유지
with open("./input.txt", "r", encoding="utf-8") as input_file:
    input_content = input_file.readlines()

with open("./output.txt", "r", encoding="utf-8") as output_file:
    output_content = output_file.readlines()

# 필터링은 그대로 유지
input_content = [
    line for line in input_content if not re.match(r"^\d+(\.\d+)*\.", line.strip())
]
output_content = [
    line for line in output_content if not re.match(r"^\d+(\.\d+)*\.", line.strip())
]

combined_content = []

for english_paragraph, korean_paragraph in zip(input_content, output_content):
    combined_content.append(english_paragraph)
    combined_content.append("\n")
    combined_content.append(korean_paragraph)
    combined_content.append("\n")

# combined.txt 파일을 새로 생성하거나 덮어씌움
with open(combined_filepath, "w", encoding="utf-8") as combined_file:
    combined_file.writelines(combined_content)
