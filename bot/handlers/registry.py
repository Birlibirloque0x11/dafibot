from telegram.ext import CommandHandler

from . basic import start
from . room import room, room_enter, room_exit

def add_handlers(dispatcher):
  def add(cmd, handler):
    dispatcher.add_handler(CommandHandler(cmd, handler))

  add('start', start)
  add('dafi', room)
  add('entro', room_enter)
  add('salgo', room_exit)
