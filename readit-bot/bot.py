#!/usr/bin/env python

# I got the code from:
#https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq

"""
Simple Telegram Bot to get a url and reply it in a form which activetes read aloud android function

Usage:
Send the page's url to the bot, it will return a 'google.readit' url

Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from URLToGoogleReadURL import to_readit_url
from URLScrapper import get_links_of_url

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def info(update, context):
    """explain bot functions"""
    text = ["This bot delivers URLs to open the 'Real Aloud' Google Assistent function",
            "To do this send it any web page's link like: 'www.example.com'",
            "Another option is to send '/table www.example.com'",
            "The /table function finds all links on the given web page"
          + " and return them individually on the Read Aloud link format",
            "This option is great for a book's table of content!"]
    for phrase in text:
        update.message.reply_text(phrase)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Give me a page's URL, I'll return it but different...")
    update.message.reply_text("Send '/help' for more information")

def get_table(update, context):
    """transform all urls of given address"""
    for link in get_links_of_url(context.args[0]):
        update.message.reply_text(to_readit_url(link))

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(to_readit_url(update.message.text))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

  # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("table", get_table))
    dp.add_handler(CommandHandler("help", info))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()