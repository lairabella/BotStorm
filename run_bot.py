from telegram.ext import Updater, CommandHandler



def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")

def talk(bot, update):
  update.message.reply_text("How are you?")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater('624266682:AAGGxwa_ZRSzDdJknM9gpCryDvmvhItebkY')
  dispatcher = updater.dispatcher
  print("Bot started")


  # Add command handler to dispatcher

  dispatcher.add_handler(CommandHandler("start", start))

  dispatcher.add_handler(CommandHandler("talk", talk))


  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
        main()