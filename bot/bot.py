from os import getenv
from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler

from bot.handlers import add_handlers

def start_bot():
  updater = Updater(token=getenv('BOT_TOKEN'))

  print('Adding handlers...')
  add_handlers(updater.dispatcher)

  print()
  print('Bot started!')
  updater.start_polling()
