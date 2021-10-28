import sys
import backtrace
import traceback
from typing import Optional
import logging
import datetime
import os

TELEGRAM_INSTALLED = False
TELEGRAM_CACHE = os.path.join(os.path.dirname(__file__), "cache.txt")

try:
    import telegram

    TELEGRAM_INSTALLED = True
except ImportError:
    pass


def send_telegram_message(token, chat_ids, message):
    try:
        bot = telegram.Bot(token)
        for chat_id in chat_ids:
            bot.sendMessage(chat_id=str(chat_id), text=message)
    except telegram.error.TelegramError as e:
        logging.warning(f"sweetdebug : telegram error, {e}, {type(e)}")


def load_cache():
    with open(TELEGRAM_CACHE) as f:
        contents = f.readlines()
    telegram_api_token = contents[0].strip()
    chat_ids = [chat_id.strip() for chat_id in contents[1:]]
    return telegram_api_token, chat_ids


def save_cache(telegram_api_token: str, chat_ids: list):
    with open(TELEGRAM_CACHE, "w") as f:
        f.writelines("\n".join([telegram_api_token] + chat_ids))


def sweetdebug(
    telegram_api_token: Optional[str] = None,
    chat_ids: Optional[list] = None,
    use_telegram_if_cache_exists=True,
    save_telegram_cache=True,
):
    """
    :param telegram_api_token:
        - (str) "11234565445:AEAL7G_VGFDRKwvHD8OXca5e2EnZBAHaTw"

    :param chat_ids:
        - (str) '34903284'
        - (int) 34903284
        - (list) ['34903284', '34903285']

    :param use_telegram_if_cache_exists:
        <cache>
        - informations of telegram token above will be automatically saved. This is "cache file".

    :param save_telegram_cache:
        - if True, telegram token and chat ids will be saved.

    :return:
    """
    backtrace.hook(align=True)
    old_hook = sys.excepthook

    if isinstance(chat_ids, str) or isinstance(chat_ids, int):
        chat_ids = [chat_ids]

    if use_telegram_if_cache_exists and os.path.exists(TELEGRAM_CACHE):
        telegram_api_token, chat_ids = load_cache()

    if telegram_api_token is not None and chat_ids is not None and save_telegram_cache:
        save_cache(telegram_api_token=telegram_api_token, chat_ids=chat_ids)

    def new_hook(type_, value, tb):
        old_hook(type_, value, tb)
        if telegram_api_token is not None and chat_ids is not None:
            if not TELEGRAM_INSTALLED:
                logging.warning(
                    f"sweetdebug : It seems that telegram module is not installed. Try 'pip install python-telegram-bot'"
                )
            else:
                message = f"{datetime.datetime.now()}\n"
                message += "\n".join(traceback.format_exception(type_, value, tb))
                send_telegram_message(
                    token=telegram_api_token, chat_ids=chat_ids, message=message
                )

        if type_ != KeyboardInterrupt:
            import pdb

            pdb.post_mortem(tb)

    sys.excepthook = new_hook
