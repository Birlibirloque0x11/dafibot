DAFI Bot
========

## Requirements

This bot requires **Python 3.6** or higher and **pip3**. The following libraries must be installed:

* python-dotenv
* python-telegram-bot

There must be a `.env` file created in the bot directory with the following entries:

* `BOT_TOKEN`: Telegram bot token
* `DAFI_MEMBERS`: Comma-separated list of the DAFI members in the following syntax: TELEGRAM_ID:MEMBER_NAME

The bot must run in a virtual env created using the following command:

```bash
python3 -m venv venv
```

## Run

To run the bot execute the following command:

```bash
python -m bot
```
