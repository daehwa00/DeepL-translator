# Text translation tool using DeepL

이 프로젝트는 DeepL API를 활용하여 텍스트 파일의 내용을 번역하는 파이썬 스크립트입니다. 사용자는 영어로 된 텍스트 파일을 input.txt에 입력하면, 스크립트가 해당 내용을 한국어로 번역하여 combined.txt에 저장합니다.

### Requirements

- Python
- DeepL API 키가 필요합니다. (DeepL 계정 생성 후 API 키를 발급받으세요.)

### Install

1. 이 프로젝트의 저장소를 복제합니다.

```

git clone https://your-repository-url-here

```

2. DeepL 패키지를 설치합니다.

```

pip install deepl

```

3. `config.json` 파일에 DeepL API 키를 입력합니다.

```json
{
  "auth_key": "여기에_당신의_API_키를_입력하세요"
}
```

4. `input.txt` 파일에 번역하고자 하는 영어 텍스트를 입력합니다.

### 사용 방법

스크립트를 실행하려면, 다음 명령어를 사용합니다:

```

python translator.py

```

이 명령어를 실행한 후, 스크립트는 `input.txt`에 있는 텍스트를 읽어 한국어로 번역하고, 번역된 내용을 `output.txt`에 저장합니다. 또한, 원본 영어 텍스트와 번역된 한국어 텍스트가 번갈아가며 포함된 `combined.txt` 파일도 생성됩니다.

## 기능

- **텍스트 번역**: `input.txt` 파일의 영어 텍스트를 한국어로 번역합니다.
- **결과 저장**: 번역된 텍스트를 `output.txt` 파일에 저장합니다.
- **병렬 텍스트 파일 생성**: 원본 텍스트와 번역된 텍스트를 포함한 `combined.txt` 파일을 생성합니다.

## 개발자를 위한 정보

이 프로젝트는 개방형 소프트웨어 라이선스 하에 제공됩니다. 자유롭게 수정하고 재배포할 수 있습니다. 버그 발견 시 이슈 트래커를 통해 보고해 주세요.
