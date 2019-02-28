from os import getenv

members = {}

for m in getenv('DAFI_MEMBERS').split(','):
  id, name = m.split(':')

  members[int(id)] = name

inside = set()

def room(bot, update):
  msg = 'Ahora mismo no hay nadie en DAFI'

  if len(inside) > 0:
    msg = 'Ahora mismo están en DAFI:'

    for m in inside:
      msg += '\n + ' + members[m]

  bot.send_message(chat_id=update.message.chat_id, text=msg)

def room_enter(bot, update):
  id = update.message.chat.id

  msg = 'El inventario está lleno'

  if id in inside:
    msg = 'Ya estás en DAFI'
  elif id in members:
    inside.add(id)

    msg = 'Acabas de entrar a DAFI'

  bot.send_message(chat_id=update.message.chat_id, text=msg)

def room_exit(bot, update):
  id = update.message.chat.id

  msg = 'El inventario está lleno'

  if id in inside:
    inside.remove(id)

    msg = 'Acabas de salir de DAFI'
  elif id in members:
    msg = 'No estás en DAFI'

  bot.send_message(chat_id=update.message.chat_id, text=msg)
