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
