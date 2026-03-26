# pysetup-uv

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?logo=astral&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-only-0078D4?logo=windows&logoColor=white)

uv 기반 Python 개발환경을 빠르게 구성하는 CLI 도구입니다.  
새 프로젝트 폴더에서 `pysetup` 한 줄로 가상환경 생성, 프로젝트 파일 생성, 패키지 동기화까지 한번에 처리합니다.

<br>

## 🛠 기술 스택

| 구분        | 기술             |
| ----------- | ---------------- |
| **Runtime** | Python 3.11+, uv |
| **CLI**     | Typer, Rich      |

<br>

## 📦 설치

```powershell
uv tool install git+https://github.com/sebalnakji/pysetup-uv
```

<br>

## 🚀 사용법

새 프로젝트 폴더로 이동 후 실행합니다.

```powershell
pysetup
```

### 1. 메뉴

| 번호 | 기능             | 설명                                                  |
| ---- | ---------------- | ----------------------------------------------------- |
| 1    | 환경구성         | 가상환경 생성 + 프로젝트 파일 생성 + `uv sync`        |
| 2    | Python 버전 변경 | 기존 `.venv` 삭제 후 지정 버전으로 재생성 + `uv sync` |

### 2. 생성되는 파일

| 파일                    | 설명                    |
| ----------------------- | ----------------------- |
| `.venv/`                | 가상환경                |
| `pyproject.toml`        | 의존성 및 프로젝트 설정 |
| `.gitignore`            | git 제외 목록           |
| `.env`                  | 환경변수                |
| `src/`                  | 소스 폴더               |
| `README.md`             | 프로젝트 설명           |
| `.vscode/settings.json` | VS Code 인터프리터 설정 |

> 이미 존재하는 파일은 덮어쓰지 않습니다.

### 3. 패키지 관리

```powershell
uv add requests      # 패키지 추가
uv remove requests   # 패키지 제거
uv sync              # pyproject.toml 기준 동기화
```

<br>

## 🔄 업데이트

```powershell
uv tool upgrade pysetup-uv
```

<br>

## 🔧 트러블슈팅

### 1. `pysetup` 명령어를 인식하지 못하는 경우

**원인:** `C:\Users\<username>\.local\bin`이 PATH에 등록되지 않은 경우

**해결 1 — 영구 등록**

> 시작 → 환경변수 편집 → 사용자 변수 → Path → 편집 → `C:\Users\<username>\.local\bin` 추가

**해결 2 — 현재 터미널에서 임시 적용**

```powershell
$env:PATH = [Environment]::GetEnvironmentVariable("PATH", "User") + ";" + [Environment]::GetEnvironmentVariable("PATH", "Machine")
```

### 2. VS Code 터미널에서 인식하지 못하는 경우

**원인:** VS Code 터미널이 환경변수 변경을 즉시 반영하지 못하는 경우

**해결:** VS Code `settings.json`에 아래 내용을 추가합니다.

```json
"terminal.integrated.env.windows": {
    "PATH": "C:\\Users\\<username>\\.local\\bin;${env:PATH}"
}
```
