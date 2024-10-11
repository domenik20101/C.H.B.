import telebot
from config import token
from maps import plate_draw, mall_draw

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    welcome_text = (
        "Привет! Я твой бот.\n"
        "Доступные команды:\n"
        "/plate - Получить изображение 'plate'\n"
        "/mall - Получить изображение 'mall'"
    )
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=["plate"])
def plate(message):
    plate_draw()
    with open("out.png", "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=["mall"])
def mall(message):
    mall_draw()
    with open("out1.png", "rb") as f:
        bot.send_photo(message.chat.id, f)

bot.polling(non_stop=True)
