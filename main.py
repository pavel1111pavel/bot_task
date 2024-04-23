import requests
from telegram.ext import Updater, CommandHandler

# Замените URL_API на URL вашего API
API_URL = "http://example.com/api/"

def start(update, context):
    update.message.reply_text("Привет! Я бот для работы с вашим API. Отправь мне команду /get_data, чтобы получить данные.")

def get_data(update, context):
    response = requests.get(API_URL + "data/")
    if response.status_code == 200:
        data = response.json()
        update.message.reply_text("Получены данные: {}".format(data))
    else:
        update.message.reply_text("Не удалось получить данные с сервера.")

def set_data(update, context):
    # Здесь вы можете предусмотреть логику для отправки данных на ваше API
    pass

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get_data", get_data))
    dp.add_handler(CommandHandler("set_data", set_data))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
