# 📖 Verse Finder Telegram Bot

A professional Telegram bot designed to help users find biblical verses () based on Jewish traditions. Developed with Python and the `python-telegram-bot` library.

---

## 🌟 Overview
In Jewish tradition, it is common to recite a verse at the end of the 'Amidah' prayer that starts with the first letter of one's name and ends with the last. This bot automates that search and offers additional ways to find verses connected to a person's name.

---

## ✨ Key Features

- 🔤 **Edge Matching** – Finds verses starting with the first letter and ending with the last letter of a given name.
- 🔎 **Name Inclusion** – Finds verses where a specific name appears inside the text.
- 🔄 **Hybrid Mode** – Combines both search strategies for maximum coverage.
- 📜 **Smart Pagination** – Automatically splits long verses into multiple Telegram messages to respect character limits.
- 📊 **Admin Analytics** – Tracks unique users and engagement statistics.
- 🧪 **Tested Core Logic** – Unit tests ensure correctness and maintainability.
- 🐳 **Dockerized** – Fully containerized for consistent environments.
- ☁️ **Cloud Deployed** – Running in production on Railway.

---

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Bot Framework:** python-telegram-bot (async, v20+)
- **Configuration:** python-dotenv
- **Testing:** pytest
- **Containerization:** Docker
- **Deployment:** Railway
- **Data Source:** Sefaria biblical database

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/NoamCohen12/tanach-verse.git
cd tanach_verse
```
Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
BOT_TOKEN=your_telegram_bot_token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

You can use `.env.example` as a template.

---


## ▶️ Running the Telegram Bot

```bash
python adapters/telegram_bot.py
```

---
## 📁 Project Structure

```
tanach_verse/
│
├── adapters/
│   ├── flask_app.py          # Flask HTTP API interface
│   ├── telegram_bot.py       # Telegram bot entry & handlers
│   └── users.json            # Local user storage (analytics)
│
├── analytics/
│   └── users.py              # User tracking logic
│
├── core/
│   ├── finder.py             # Verse search engine
│   └── hebrew.py             # Hebrew normalization utilities
│
├── data/
│   ├── tanach.json           # Raw Tanach dataset
│   └── tanach_clean.json     # Processed dataset (niqqud removed)
│
├── scripts/
│   ├── clean_nikud.py        # Removes niqqud from dataset
│   ├── download_tanach.py    # Dataset downloader
│   └── hebraize_tanach_data.py
│
├── tests/
│   ├── test_finder.py
│   ├── test_hebraize.py
│   └── test_hebrew.py
│
├── .env
├── .env.example
├── Dockerfile
└── README.md
```

---
👨‍💻 Developed By
Noam Cohen

📜 Credits
Biblical data provided by Sefaria.org.