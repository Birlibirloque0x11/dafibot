from telegram.ext import CommandHandler

from . basic import start

def add_handlers(dispatcher):
  def add(cmd, handler):
    dispatcher.add_handler(CommandHandler(cmd, handler))

  add('start', start)
