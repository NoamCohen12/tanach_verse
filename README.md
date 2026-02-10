# 📖 Verse Finder Telegram Bot

A professional Telegram bot designed to help users find biblical verses () based on Jewish traditions. Developed with Python and the `python-telegram-bot` library.

---

## 🌟 Overview
In Jewish tradition, it is common to recite a verse at the end of the 'Amidah' prayer that starts with the first letter of one's name and ends with the last. This bot automates that search and offers additional ways to find verses connected to a person's name.

## ✨ Key Features
* **🔤 Edge Matching:** Finds verses starting with the first letter and ending with the last letter of a name.
* **🔎 Name Inclusion:** Finds verses where the specific name appears within the text.
* **🔄 Hybrid Mode:** Performs both searches simultaneously for maximum results.
* **📊 Admin Dashboard:** Built-in analytics to track unique user engagement.
* **📜 Smart Pagination:** Handles long biblical texts by splitting them into multiple messages to avoid Telegram's character limits.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Framework:** [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (Asynchronous)
* **Configuration:** `python-dotenv`
* **Data Source:** Integration with Sefaria's biblical database.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/verse-finder-bot.git](https://github.com/your-username/verse-finder-bot.git)
   cd verse-finder-bot
Install dependencies:

Bash
pip install -r requirements.txt
Set up Environment Variables: Create a .env file in the root directory:

Configuration: The bot requires environment variables to run.

Use the template provided in env_example to create your own .env file.

Fill in your Telegram Bot Token and Admin ID inside the .env file.

Run the application:

Bash
python main.py
📂 Project Structure
main.py: Entry point and Telegram bot handlers.

core/finder.py: Logic for searching and filtering verses.

analytics/users.py: User tracking and statistics.

env_example: Template for environment variables.

👨‍💻 Developed By
Noam Cohen

📜 Credits
Biblical data provided by Sefaria.org.