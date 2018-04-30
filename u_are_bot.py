from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
import logging
import config

logging.basicConfig(level=logging.INFO, filename="./u_are_bot.log") 

#U_ARE_BOT_TOKEN = '556325340:AAHLaBMJUHUJzAfyiBRrkfkdaFq9D9r5-DQ'


def start_bot(bot, update):
    '''Sends "Hi" when user sends /start command'''
    update.message.reply_text('Привет!')


def echo(bot, update):
    '''Echo user's message'''
    update.message.reply_text('Ты ' + update.message.text)


def main():
    '''Config bot and start'''
    updater = Updater(config.U_ARE_BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    


