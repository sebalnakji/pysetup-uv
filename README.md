# pysetup-uv

uv 기반 Python 개발환경을 빠르게 구성하는 CLI 도구입니다. (Windows 전용)

## 요구사항

- Windows
- [uv](https://github.com/astral-sh/uv) 설치 필요

## 설치

```bash
uv tool install git+https://github.com/sebalnakji/pysetup-uv
```

## 업데이트

```bash
uv tool upgrade pysetup-uv
```

## 사용법

새 프로젝트 폴더로 이동 후 실행:

```bash
pysetup
```

### 메뉴

| 번호 | 기능             | 설명                                                  |
| ---- | ---------------- | ----------------------------------------------------- |
| 1    | 환경구성         | `.venv` 생성 + 프로젝트 파일 생성 + `uv sync`         |
| 2    | Python 버전 변경 | 기존 `.venv` 삭제 후 지정 버전으로 재생성 + `uv sync` |

### 생성되는 파일

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

### 패키지 동기화

`pyproject.toml`에 의존성 추가 후:

```bash
uv sync
```
