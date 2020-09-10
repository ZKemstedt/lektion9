# Lesson 9 - File handling and Databases

## Setup

1. Create a virtual environment
2. Install requirements
3. [Optional] Install extensions for Visual Studio Code
4. [Optional] Enable linting for Visual Studio Code

### Virtual environment (venv)

see <https://docs.python.org/3/library/venv.html>

Windows - cmd.exe

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell

```PowerShell
# You  On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### Install requirements.txt

```bat
pip install -r requirements.txt
```

### Recommended Visual Studio Code - Extensions

- sqlite see <https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite>
- markdown-all-in-one see: <https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one>

### Setup linting in Visual Studio Code

1. Open settings.json in .vscode
2. Add config for linting:

```json
    "python.linting.mypyEnabled": true,
    "python.linting.flake8Enabled": true
```
