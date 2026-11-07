import telebot

from dotenv import load_dotenv  

import os  

from buttons import Buttons  

load_dotenv()  

API_TOKEN = os.environ.get("TOKEN")  

bot = telebot.TeleBot(API_TOKEN)  

buttons = Buttons(bot)  

@bot.message_handler(commands=["start"])  
def send_welcome(message):
    markup = buttons.main_menu()  


    bot.send_message(
        message.chat.id,  
    

        """سلام! به ربات پیشنهاد خرید خوش اومدی.\n"""
        """از منو یکی از گزینه‌ها رو انتخاب کن.""",  
    

        reply_markup=markup  
    
    )

if __name__ == "__main__":  


    print("Bot is running...")  


    bot.infinity_polling()  

