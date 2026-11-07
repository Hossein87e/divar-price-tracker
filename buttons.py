from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from scraper import search_and_scrape
import json
last_message = {}
user_state = {}


class Buttons:
    def __init__(self, bot):
        self.bot = bot
        self.register_callbacks()

    def main_menu(self):
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("جستجو در دیوار", callback_data="search"),
            InlineKeyboardButton("راهنما", callback_data="help"),
        )
        return markup

    def register_callbacks(self):
        self.bot.register_callback_query_handler(
            self.callback_handler, func=lambda call: True
        )

    def callback_handler(self, call):
        chat_id = call.message.chat.id

        if call.data == "help":
            self.bot.send_message(chat_id,
                "اسم ماشین، خانه یا هر چیزی را وارد کن.\n"
                "مثال: پراید، 206، آپارتمان 80 متری"
            )

        elif call.data == "search":
            sent = self.bot.send_message(
                chat_id,
                "چی می‌خوای؟ اسمش رو بگو (مثلاً: پراید یا 206)"
            )
            user_state[chat_id] = {"step": "query"}
            self.bot.register_next_step_handler(sent, self.get_query)

    def get_query(self, message):
        chat_id = message.chat.id
        query = message.text.strip()

        user_state[chat_id]["query"] = query

        sent = self.bot.send_message(
            chat_id,
            "چند آگهی می‌خوای؟ (مثلاً: 10)"
        )
        user_state[chat_id]["step"] = "limit"
        self.bot.register_next_step_handler(sent, self.get_limit)

    def get_limit(self, message):
        chat_id = message.chat.id
        limit = int(message.text.strip())

        query = user_state[chat_id]["query"]

        self.bot.send_message(chat_id, "در حال جستجو و اسکرپ... لطفاً صبر کن.")

        result = search_and_scrape(query, limit)


        text = json.dumps(result, ensure_ascii=False, indent=2)

        self.bot.send_message(chat_id, f"نتیجه:\n{text}")
