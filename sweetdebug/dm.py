import sys
import backtrace
import traceback
from typing import Union
import logging
import datetime


TELEGRAM_INSTALLED = False
try:
    import telegram

    TELEGRAM_INSTALLED = True
except ImportError:
    pass


def send_telegram_message(token, chat_ids, message):
    try:
        bot = telegram.Bot(token)
        if isinstance(chat_ids, str) or isinstance(chat_ids, int):
            bot.sendMessage(chat_id=str(chat_ids), text=message)
        else:
            for chat_id in chat_ids:
                bot.sendMessage(chat_id=str(chat_id), text=message)
    except telegram.error.TelegramError as e:
        logging.warning(f"sweetdebug : telegram error, {e}, {type(e)}")


def sweetdebug(
    telegram_api_token: Union[None, str] = None, chat_ids: Union[None, list] = None
):
    backtrace.hook(align=True)
    old_hook = sys.excepthook

    def new_hook(type_, value, tb):
        old_hook(type_, value, tb)
        if telegram_api_token is not None and chat_ids is not None:
            if not TELEGRAM_INSTALLED:
                logging.warning(
                    f"sweetdebug : It seems that telegram module is not installed. Try 'pip install python-telegram-bot'"
                )
            else:
                now = datetime.datetime.now()
                prefix = f"{now}\n"
                message = "\n".join(traceback.format_exception(type_, value, tb))
                message = prefix + message
                send_telegram_message(
                    token=telegram_api_token, chat_ids=chat_ids, message=message
                )

        if type_ != KeyboardInterrupt:
            import pdb

            pdb.post_mortem(tb)

    sys.excepthook = new_hook
