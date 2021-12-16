import telebot

bot = telebot.TeleBot("1812157729:AAGuH6YMqxbD5skElFUW250UWW7z017yJv0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
     bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
