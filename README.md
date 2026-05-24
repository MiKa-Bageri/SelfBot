SelfBot

A simple Telegram selfbot built with Pyrogram and SQLite.
This project supports auto replies, greeting messages, customer management, and public messaging features.

Because apparently humans decided one Telegram account should work like a tiny customer support department running on caffeine and questionable life choices.

Features
Auto greeting for private chats
Quick reply system
Public/broadcast messaging
Customer management
SQLite database support
Userbot commands
Lightweight and simple structure

SelfBot/
│
├── main.py
├── config.py
├── database.db
│
├── helpers/
│   ├── greeting.py
│   ├── public_msgs.py
│   └── quick_replys.py
│
├── modules/
│   └── db.py
│
└── plugins/
    └── commands.py

Installation
1. Clone the repository
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY

2. Install requirements
pip install -r requirements.txt

Configuration

Edit config.py:
API_ID = 123456
API_HASH = "your_api_hash"
SESSION = "your_session_string"

Run the bot
python main.py

Commands
| Command    | Description           |
| ---------- | --------------------- |
| `add`      | Mark user as customer |
| `همگانی`   | Send public message   |

Technologies Used
Python
Pyrogram
SQLite
aiosqlite

Warning

Using selfbots may violate Telegram's Terms of Service.
Heavy automation, spam, or aggressive messaging can result in account limitations or bans.

Telegram tolerates automation right up until it suddenly develops strong moral principles at 3 AM and rate-limits your account into oblivion.