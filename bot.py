import telebot

bot = telebot.TeleBot('7541820284:AAFb6qFZkFcbtaGqzUXlDde-bDKBsxTUHUg')
@bot.message_handler(content_types=['text','photo'])
def get_bag(message):
    if message.text == '/start':
        pass
    else:
        if message.from_user.id == 1889210692:
            t = message.text.split()
            t.pop(-1)
            t = ' '.join(t)
            try:
                bot.send_message(int(message.text.split()[-1]) ,t)
            except Exception as error:
                bot.send_message(1889210692 ,error)    
        else:
            if message.photo == None:
                try:
                    bot.send_message(1889210692, message.text + ' ' + str(message.from_user.id))
                except:
                    pass
            else:
                try:
                    bot.send_message(1889210692, message.text + ' ' + str(message.from_user.id))
                except:
                    pass
                bot.send_photo(1889210692,message.photo[-1].file_id)
                bot.send_message(1889210692 ,str(message.from_user.id))
bot.polling(none_stop=True,interval=0)
