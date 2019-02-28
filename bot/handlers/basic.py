def start(bot, update):
  print(update)

  bot.send_message(chat_id=update.message.chat_id, text="Hola {}, soy el DAFI Bot. ¿En qué puedo ayudarte?".format(update.message.chat.first_name))
