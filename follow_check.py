import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
INSTA_USERNAME = os.getenv("INSTA_USERNAME")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")

cl = Client()

def login_instagram():
    try:
        if os.path.exists("session.json"):
            try:
                cl.load_settings("session.json")
                cl.login(INSTA_USERNAME, INSTA_PASSWORD)
                return True
            except Exception:
                pass
        
        cl.set_device({
            "app_version": "269.0.0.18.75",
            "manufacturer": "Samsung",
            "model": "Galaxy S23"
        })
        
        cl.login(INSTA_USERNAME, INSTA_PASSWORD)
        cl.dump_settings("session.json")
        return True

    except Exception as e:
        print(f"Login Error: {e}")
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot online. Usage: /analyze <username>"
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please enter a username.")
        return

    target_username = context.args[0]
    await update.message.reply_text(f"Analyzing {target_username}...")

    try:
        user_id = cl.user_id_from_username(target_username)
        
        followers_list = cl.user_followers_v1(user_id, amount=0)
        following_list = cl.user_following_v1(user_id, amount=0)

        followers_set = {user.pk for user in followers_list}
        following_dict = {user.pk: user.username for user in following_list}
        following_set = set(following_dict.keys())

        unfollowers_ids = following_set - followers_set
        unfollowers = [following_dict[uid] for uid in unfollowers_ids]
        
        message = (
            f"Analysis Result:\n"
            f"Target: {target_username}\n"
            f"Followers: {len(followers_list)}\n"
            f"Following: {len(following_list)}\n"
            f"Not Following Back: {len(unfollowers)}"
        )
        await update.message.reply_text(message)

        if len(unfollowers) > 0:
            filename = f"{target_username}_unfollowers.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(unfollowers))
            
            with open(filename, 'rb') as doc_file:
                await update.message.reply_document(document=doc_file)
            
            os.remove(filename)
        else:
            await update.message.reply_text("Everyone is following back!")

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
        if "login_required" in str(e):
             login_instagram()

if __name__ == '__main__':
    if login_instagram():
        print("Bot is running...")
        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("analyze", analyze))
        app.run_polling()
    else:
        print("Login failed.")
