#🧠 JARVIS - AI-Powered Personal Voice Assistant

JARVIS is a Python-based voice assistant designed to perform various tasks such as speech recognition, 
AI interaction using OpenAI & Gemini, image generation, emailing, WhatsApp messaging, task tracking, and more – all via simple voice commands.

#🚀 Features

- 🎙️ **Voice Command Recognition** using Google Speech API  
- 🗣️ **Text-to-Speech Response** with `pyttsx3`  
- 🌐 **Google Search & Wikipedia Summary**  
- 📅 **To-Do Management** (create, view tasks, notify)  
- 🎵 **Music Playback via YouTube**  
- 🖼️ **Image Generation** using Replicate API  
- 🤖 **AI Interactions** via OpenAI GPT & Google Gemini  
- 📧 **Email Sending** via Gmail  
- 💬 **Send WhatsApp Messages** with PyWhatKit  
- 💻 **Desktop App Launcher**  
- 🔐 **Secure Configuration** through `user_config.py`

#🧰 Tech Stack

- **Python Libraries**: `pyttsx3`, `speech_recognition`, `pyautogui`, `pywhatkit`, `wikipedia`, `plyer`, `requests`, `smtplib`, `ssl`, `replicate`, `mtranslate`
- **AI Services**: OpenAI GPT-4o, Gemini Pro, Replicate (for image generation)
- **Other Tools**: `Pillow`, `WebBrowser`, `PyAudio`

#🗂️ Folder Structure

```
.
├── main.py                # Main JARVIS logic and voice command loop
├── speech.py              # Speech recognition using multiple providers
├── openai_request.py      # Handles OpenAI and Gemini requests
├── image_generation.py    # Image generation using Replicate API
├── user_config.py         # Stores keys and credentials (keep secure!)
├── todo.txt               # Text file for task list storage
├── PyWhatKit_DB.txt       # WhatsApp message log
```

#🛠️ Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API Keys** in `user_config.py`:
   - Gmail password
   - OpenAI key
   - Gemini API key

4. **Run the assistant**:
   ```bash
   python main.py
   ```

> 🔐 **Note**: Keep your `user_config.py` file secure and avoid pushing it to public repositories.

#📌 Sample Voice Commands

- "Hello"
- "Play music"
- "Say time"
- "New task Finish homework"
- "Speak task"
- "Search Wikipedia for Albert Einstein"
- "Search Google Artificial Intelligence"
- "Send email"
- "Send WhatsApp"
- "Create an image of a futuristic city"
- "Ask AI tell me a joke"
- "Ask Gemini what's the weather in Delhi?"

#🤝 Contributions

Contributions are welcome! Please fork the repository and submit a pull request.

