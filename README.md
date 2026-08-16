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

### 6. Use the Message Function 📱

Jarvis can also send WhatsApp messages using **PyWhatKit**. To use this feature, you need to create a separate Python file to store the names and phone numbers of your contacts.

#### Create `numbers_phone.py`

In the same folder as `main.py`, create a new file called:

```text
numbers_phone.py
```

Inside the file, create a dictionary containing the names and phone numbers of your contacts:

```python
numbers = {
    "alice": "+919xxxxxxx",
    "bob": "+917xxxxxxxxx",
}
```

Replace these names and phone numbers with your own contacts.

> **Important:** Store phone numbers as strings and include the country code, for example `+91` for India.

#### Import the Contact Dictionary

In `main.py`, import the dictionary:

```python
from numbers_phone import numbers
```

Jarvis will use the name you speak to look up the corresponding phone number from the dictionary.

#### How to Send a Message

Run Jarvis normally:

```bash
python main.py
```

Then say:

```text
Jarvis
```

After Jarvis responds, say:

```text
send a message
```

Jarvis will then ask you for:

1. **The contact's name** — for example, `alice`
2. **The message** — for example, `Hey alice, how are you?`

Jarvis will look up the phone number associated with the name in `numbers_phone.py` and use **PyWhatKit** to send the WhatsApp message.

For example:

```text
You: Jarvis
Jarvis: hello

You: send a message

Jarvis: Name...
You: Saad

Jarvis: Message...
You: Hey alice, how are you?
```

The program will find:

```python
numbers.get("alice")
```

which returns:

```text
+919xxxxxxx
```

and then sends the message through WhatsApp.

#### ⚠️ Privacy & Security

Do **not** upload `numbers_phone.py` to a public GitHub repository if it contains real people's phone numbers.

Add it to `.gitignore`:

```text
numbers_phone.py
```

A safer approach is to provide an example file such as:

```text
numbers_phone.example.py
```

containing dummy numbers:

```python
numbers = {
    "example": "+910000000000",
}
```

Then each user can create their own `numbers_phone.py` locally.

Your `.gitignore` could contain:

```text
.env
numbers_phone.py
```

