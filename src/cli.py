from rich.console import Console
from rich.prompt import Prompt

from pysetup_uv import core

console = Console()
DEFAULT_PYTHON = "3.11"


def main() -> None:
    console.print("\n[cyan]===========================================[/cyan]")
    console.print("[cyan]   🚀 Python 프로젝트 환경 관리 (with uv)   [/cyan]")
    console.print("[cyan]===========================================[/cyan]\n")
    console.print("  [white][1] 환경구성        - 가상환경 생성 + 파일 생성 + uv sync[/white]")
    console.print("  [white][2] Python 버전 변경 - 기존 .venv 삭제 후 재생성[/white]\n")

    choice = Prompt.ask("선택", choices=["1", "2"])

    if choice == "1":
        python_ver = Prompt.ask(f"\n🐍 Python 버전 (엔터 = {DEFAULT_PYTHON})", default=DEFAULT_PYTHON)
        core.create_venv(python_ver)
        core.create_project_files(python_ver)
        core.sync_packages()
        console.print("\n[cyan]🎉 환경구성 완료! VS Code를 재실행하거나 터미널을 다시 여세요.[/cyan]")

    elif choice == "2":
        python_ver = Prompt.ask(f"\n🐍 Python 버전 (엔터 = {DEFAULT_PYTHON})", default=DEFAULT_PYTHON)
        core.remove_venv()
        core.create_venv(python_ver)
        core.sync_packages()
        console.print(f"\n[cyan]🎉 Python {python_ver} 환경으로 변경 완료! VS Code를 재실행하세요.[/cyan]")