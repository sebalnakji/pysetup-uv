import shutil
import subprocess
import sys
from pathlib import Path

from rich.console import Console

console = Console()


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd)
    if result.returncode != 0:
        console.print(f"[red]❌ 실패: {' '.join(cmd)}[/red]")
        sys.exit(1)


def create_venv(python_ver: str) -> None:
    console.print(f"\n[yellow]가상환경 생성 중 (Python {python_ver})...[/yellow]")
    run(["uv", "venv", "--python", python_ver])
    console.print("[green]✅ 가상환경 생성 완료[/green]")


def remove_venv() -> None:
    venv = Path(".venv")
    if venv.exists():
        console.print("\n[yellow]기존 .venv 삭제 중...[/yellow]")
        shutil.rmtree(venv)
        console.print("[green]✅ .venv 삭제 완료[/green]")


def sync_packages() -> None:
    console.print("\n[yellow]패키지 동기화 중 (uv sync)...[/yellow]")
    run(["uv", "sync"])
    console.print("[green]✅ 패키지 동기화 완료[/green]")


def create_project_files(python_ver: str) -> None:
    _write_if_not_exists(
        "pyproject.toml",
        f'[project]\nname = "my-project"\nversion = "0.1.0"\nrequires-python = ">={python_ver}"\ndependencies = []\n\n[build-system]\nrequires = ["hatchling"]\nbuild-backend = "hatchling.build"\n',
    )
    _write_if_not_exists(".gitignore", ".venv/\n__pycache__/\n*.pyc\n.env\ndist/\nbuild/\n")
    _write_if_not_exists(".env", "")
    _write_if_not_exists("README.md", "# 프로젝트 이름\n")
    _mkdir_if_not_exists("src")
    _create_vscode_settings()


def _write_if_not_exists(filename: str, content: str) -> None:
    path = Path(filename)
    if path.exists():
        console.print(f"[dim]⏭️  {filename} 이미 존재 - 건너뜀[/dim]")
        return
    path.write_text(content, encoding="utf-8")
    console.print(f"[green]✅ {filename} 생성 완료[/green]")


def _mkdir_if_not_exists(dirname: str) -> None:
    path = Path(dirname)
    if path.exists():
        console.print(f"[dim]⏭️  {dirname}/ 이미 존재 - 건너뜀[/dim]")
        return
    path.mkdir()
    console.print(f"[green]✅ {dirname}/ 생성 완료[/green]")


def _create_vscode_settings() -> None:
    settings = Path(".vscode/settings.json")
    if settings.exists():
        console.print("[dim]⏭️  .vscode/settings.json 이미 존재 - 건너뜀[/dim]")
        return
    settings.parent.mkdir(exist_ok=True)
    settings.write_text(
        '{\n    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",\n    "python.terminal.activateEnvironment": true\n}\n',
        encoding="utf-8",
    )
    console.print("[green]✅ .vscode/settings.json 생성 완료[/green]")