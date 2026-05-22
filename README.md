A custom Telegram bot built with python-telegram-bot that uses OpenAI's GPT-4o-mini to act as a conversational assistant in group chats. The bot replies to mentions and direct replies, utilizing a customizable persona to drive its interactions.

🌟 Features
Group Chat Integration: Automatically responds when tagged (@your_bot_username) or when a user directly replies to one of its messages.

AI-Powered Conversations: Uses OpenAI's gpt-4o-mini model for generating contextual and smart responses.

Customizable Persona: Reads its system prompt from a local persona.txt file, allowing you to change the bot's personality on the fly.

Custom Error Handling: Includes localized (Ukrainian), humorous fallback messages for API rate limits (429) and server unavailability (503).

Modular Architecture: Handlers and services are cleanly separated into distinct modules for easy maintenance and scalability.

🚀 Prerequisites
Python 3.8 or higher.

Telegram Bot Token: Get this from @BotFather on Telegram.

OpenAI API Key: Get this from the OpenAI Developer Platform.

🛠️ Installation & Setup
Clone the repository or download the source code:

Bash
git clone <your-repository-url>
cd MRDARK_BOT

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:
Make sure your requirements.txt includes python-telegram-bot, python-dotenv, and openai.

Bash
pip install -r requirements.txt

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   AI_API_TOKEN=your_openai_api_key_here
Define the Bot's Persona:
Create or edit services/persona.txt and write the system prompt that defines how the bot should act. For example:

You are a sarcastic but helpful assistant who answers questions concisely.

   > **Note:** If this file is missing, the bot defaults to *"You are a casual chat responder."*

---

## ⚙️ Running the Bot

Start the bot by running the main script:

```bash
python main.py
You should see Bot's running in your terminal upon successful startup.

📱 Usage
/start — Wakes the bot up and returns an introductory message.

/help — Explains how to interact with the bot.

In a Group: Simply mention the bot (e.g., Hello @MRDARK_BOT, how are you?) or swipe to reply to one of its previous messages. If a user tags the bot without asking a question, it defaults to a custom prompt ("Чо малчім?").

⚠️ Notes
Privacy Mode: Make sure to disable Privacy Mode via BotFather if you want the bot to read all group messages (though currently, it is strictly filtered to only process explicit mentions and replies).

AI Settings: The current AI model is set to gpt-4o-mini with a temperature of 0.7. This can be adjusted inside services/ai_service.py.
