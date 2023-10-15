import telebot

bot = telebot.TeleBot('6584646972:AAHC4SPIU8eqizGDB73mMB9yCtMeOzCm500')

@bot.message_handlers(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Привет булочка Зубова приветствует тебя")