# Jarvis
Built a Python-based Jarvis AI assistant using Speech Recognition, Text-to-Speech, and Google Gemini API. It can understand voice commands, open websites, and answer questions using AI. 🤖🎙️
### 🤖 Jarvis AI Assistant

Jarvis is a Python-based voice assistant that uses **Speech Recognition**, **Text-to-Speech**, and **Google Gemini AI** to understand and respond to voice commands. It can open websites such as Google, YouTube, GitHub, LinkedIn, and Instagram, while Gemini provides intelligent responses to general questions.

The project is designed to evolve into a more advanced AI assistant capable of interacting with and controlling a computer through natural language commands.

## 🤖 How to Set Up Jarvis

Follow these steps to run Jarvis on your computer.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd jarvis
```

### 2. Install Required Modules

Run:

```bash
pip install SpeechRecognition pyttsx3 PyAudio google-genai python-dotenv
```

### 3. Add Your Gemini API Key

Create a file named:

```text
.env
```

Inside the `.env` file, add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your Gemini API key from **Google AI Studio**.

### 4. Update the Python Code

Make sure your code loads the API key:

```python
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
```

### 5. Run Jarvis

Start the assistant with:

```bash
python main.py
```

Say **"Jarvis"** to activate the assistant and then give it a command.

### ⚠️ Important

Never upload your `.env` file or API key to GitHub.

Add this to your `.gitignore`:

```text
.env
```

You will need to provide your own API key to use the Gemini-powered features.

Enjoy building your own Jarvis! 🤖🚀
