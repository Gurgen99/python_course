import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')


def usd(update, context):
    a = update.message.text.split(" ")
    if len(a) > 1:
        b = int(a[1]) * 517
        update.message.reply_text(b)
    else:
        update.message.reply_text("517")


def eur(update, context):
    a = update.message.text.split(" ")
    if len(a) > 1:
        b = int(a[1]) * 630
        update.message.reply_text(b)
    else:
        update.message.reply_text('630')


def rub(update, context):
    a = update.message.text.split(" ")
    if len(a) > 1:
        b = int(a[1]) * 7
        update.message.reply_text(b)
    else:
        update.message.reply_text('7')


def gbp(update, context):
    a = update.message.text.split(" ")
    if len(a) > 1:
        b = int(a[1]) * 727
        update.message.reply_text(b)
    else:
        update.message.reply_text('727')


def help(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        "1749720914:AAGYd6Mzq5XkSaqP1Nm0BIOs2Mlixl1MhvI", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("usd", usd))
    dp.add_handler(CommandHandler("eur", eur))
    dp.add_handler(CommandHandler("rub", rub))
    dp.add_handler(CommandHandler("gbp", gbp))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
