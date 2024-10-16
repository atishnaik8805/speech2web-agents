# Voice Transcription and JSON Conversion

This project provides a system for transcribing audio (both uploaded files and
live recordings) and converting the transcriptions into a structured JSON
format.

## Features

- Audio transcription using Groq API
- Conversion of transcriptions to structured JSON
- Gradio web interface for easy interaction
- Support for both uploaded audio files and live recordings

## Prerequisites

- Python 3.10 or 3.11
- Groq API key
- Internet connection for API calls

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/atishnaik8805/speech2web-agents.git
   cd speech2web-agents
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key

   Sign up for Groq Cloud from https://console.groq.com/login.

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Virtual Environment

Mamba (via [Miniforge3](https://github.com/conda-forge/miniforge)) can be used
to create a virtual environment for this project and install/update the
dependencies.

> [!TIP]
>
> - Install `miniforge3` as a standard user (non-Admin)
> - `mamba` is (mostly) interchangeable with `conda`.

```sh
# Non-elevated PowerShell terminal (may require latest version of Windows)
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
```

> [!NOTE]
>
> `spacy` blocks upgrade to Python `3.12`.

#### Run

- Open this repo using VS Code.
- Select `speech2web` as the interpreter (see bottom right).
- Run using play/run button in VS Code (see top right).

Alternatively, you may also use PowerShell to run the Python script.

```ps
& "$env:LocalAppData\miniforge3\envs\speech2web\python.exe" app.py
```

#### Upgrade

```sh
# Upgrade dependencies
mamba activate speech2web
mamba upgrade --all
```

#### Remove

Use this when upgrading Python version. Bumping Python version within an
existing environment is **not** recommended.

```sh
# Remove environment
mamba remove -n speech2web --all
```

## Usage

### Command-line Interface

To use the command-line interface for voice recording and transcription:

```
python app.py
```

This will start recording audio from your microphone, transcribe it, and output
the result.

### Gradio Web Interface

To launch the Gradio web interface:

```
python app-gradio.py
```

This will start a local web server. Open the provided URL in your browser to
access the interface, where you can:

- Upload audio files for transcription
- Record live audio for transcription
- View the transcription results and JSON conversion

## License

This project is licensed under the GNU General Public License v3.0. See the
[LICENSE](LICENSE) file for details.

## Acknowledgements

- Groq for providing the transcription API
- SpaCy for natural language processing capabilities
- Gradio for the easy-to-use web interface framework
