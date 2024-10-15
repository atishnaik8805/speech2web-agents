# Speech2Web Agents

## Development Environment

### Using Mamba

Mamba (via [Miniforge3](https://github.com/conda-forge/miniforge)) can be used
to create a virtual environment for this project and install/update the
dependencies.

> [!TIP]
>
> - Install `miniforge3` as a standard user (non-Admin)
> - `mamba` is (mostly) interchangeable with `conda`.

```sh
# Non-elevated PowerShell terminal
winget install CondaForge.Miniforge3
```

```sh
# Miniforge3 Prompt (search in Start Menu)
mamba upgrade --all

# Create virtual environment
mamba create -n speech2web
mamba activate speech2web

# Install dependencies
mamba install python=3.11
mamba install ruff pyautogen numpy requests groq python-sounddevice pysoundfile gradio
mamba install -c pytorch pytorch
mamba install spacy
pip install git+https://github.com/openai/whisper.git
```

> [!NOTE]
>
> `spacy` blocks upgrade to Python `3.12`.

#### Run

- Open this repo using VS Code.
- Select `speech2web` as the interpreter (see bottom right).
- Run using play/run button in VS Code (see top right).

Alternatively, you can also use PowerShell to run the Python script.

```ps
& "$env:LocalAppData\miniforge3\envs\speech2web\python.exe" app-gradio.py
```

#### Upgrade

```sh
# Upgrade dependencies
mamba activate speech2web
mamba upgrade --all
pip install --upgrade git+https://github.com/openai/whisper.git
```

#### Remove

Use this when upgrading Python version. Bumping Python version within an
existing environment is **not** recommended.

```sh
# Remove environment
mamba remove -n speech2web --all
```

## API Keys

- Create `.env` file in the root of this repo.
- Sign up for Groq Cloud from https://console.groq.com/login.

```py
# .env
GROQ_API_KEY = "secret"
```
