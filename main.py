import telebot
from telebot import types

bot = telebot.TeleBot("6584646972:AAHC4SPIU8eqizGDB73mMB9yCtMeOzCm500")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Привет1 {message.from_user.first_name} {message.from_user.last_name}')
    markup = types.ReplyKeyboardMarkup()
    #file = open('./clip_image002.jpg', "rb")
    #bot.send_photo(message.chat.id, file, reply_markup=markup)

@bot.message_handler(commands=['search'])
    def search(message):
        markup = types.InlineKeyboardMarkup()
        bot.reply_to(message,'Выбери как искать')
        markup.add(types.InlineKeyboardMarkup('Автор'))
        markup.add(types.InlineKeyboardMarkup('Название'))
        markup.add(types.InlineKeyboardMarkup('Журнал'))
        markup.add(types.InlineKeyboardMarkup('Общее'))



@bot.message_handler(commands=['help'])
def hselpsp(message):
    bot.reply_to(message, message)


@bot.message_handler(commands=['photo'])
def hselpsp(message):
    bot.reply_to(message, message)


@bot.message_handler()
def info(message):

    if message.text.lower() == 'привет':
        bot.reply_to(message, f'Зубкова говорит:Привет')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'твой ID:{message.from_user.id}')
    else:
        bot.reply_to(message, f'Зубкова не понимает команду: {message.text}')


bot.infinity_polling()
