Python 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import telegram
... from telegram.ext import Updater, CommandHandler
... 
... # Tokenni o'zingizning botdan olingan token bilan almashtiring
... TOKEN = 'Done! Congratulations on your new bot. You will find it at t.me/vidoes_in_subtitles_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
... 
... Use this token to access the HTTP API:
... 7523994169:AAHQid8ZNOiGw5e3YzEvn-DT-IKY7ho9sF0
... Keep your token secure and store it safely, it can be used by anyone to control your bot.
... 
... For a description of the Bot API, see this page: https://core.telegram.org/bots/api'
... 
... def start(update, context):
...     update.message.reply_text('Salom, botga xush kelibsiz!')
... 
... def main():
...     updater = Updater(TOKEN, use_context=True)
...     dispatcher = updater.dispatcher
... 
...     start_handler = CommandHandler('start', start)
...     dispatcher.add_handler(start_handler)
... 
...     updater.start_polling()
...     updater.idle()
... 
... if __name__ == '__main__':
...     main()
