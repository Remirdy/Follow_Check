# 🕵️‍♂️ Follow Check – Instagram Unfollower Detector

A Telegram bot that analyzes an Instagram account and detects users who follow the target account but do **not** follow back.  
The result is sent directly to your Telegram chat as a `.txt` file.

---

## 🚀 Features
- 🔒 **Secure Login** Saves session cookies locally (`session.json`) to avoid logging in every time and reduce the risk of triggering Instagram security checks.

- 📂 **File Output** Generates a `.txt` file containing all unfollowers.

- 📱 **Telegram Integration** Fully controlled via Telegram commands.

- 🛡️ **Stealth Mode** Emulates a real device (Samsung Galaxy S23) to bypass basic bot detection mechanisms.

---

## 🛠️ Installation

### 1️⃣ Clone the repository
git clone [https://github.com/Remirdy/Follow_Check.git](https://github.com/Remirdy/Follow_Check.git)
cd Follow_Check

### 2️⃣ Create and Activate Virtual Environment (venv)
**macos/linux**
python3 -m venv venv
source venv/bin/activate

**Windows**
python -m venv venv
venv\Scripts\activate


### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Configure the bot
Create a file named .env in the root directory and add your credentials:
TELEGRAM_TOKEN=your_token_here
INSTA_USERNAME=your_username
INSTA_PASSWORD=your_password

### Run the bot
python Follow_Check.py

🤖 Usage
1. Start the bot in Telegram: /start

2. Analyze a user:
/analiz target_username

Note: Initial login may take a few seconds as it generates the session file.)
⚠️ Disclaimer
This project is for educational purposes only. Use it at your own risk. The developer is not responsible for any actions taken by Instagram regarding your account.