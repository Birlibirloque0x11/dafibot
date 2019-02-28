if __name__ == '__main__':
  from dotenv import load_dotenv

  print('Loading ENV variables...')
  load_dotenv(verbose=True)

  from . bot import start_bot

  print('Starting bot...')
  start_bot()
