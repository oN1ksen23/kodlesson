from telebot import TeleBot

TOKEN = '6985675911:AAHjk3ylRJHidi8wGhlQgO6nTB-lXoVOHc4'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Напиши предложение и я украшу его буквы. Автор: @n1ksen23')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    text_arr = list(text)
    for i in range(len(text_arr)):
        if text_arr[i] == 'л':
            text_arr[i] = 'ᴧ'
        elif text_arr[i] == 'е' or text_arr[i] == 'ё':
            text_arr[i] = 'ᴇ'
        elif text_arr[i] == 'р':
            text_arr[i] = 'ᴩ'
        elif text_arr[i] == 'а':
            text_arr[i] = 'ᴀ'
    result = ''
    for j in text_arr:
        result += j
    print(result)
    result2 = '`'+result+'`'
    bot.send_message(message.chat.id, result2, parse_mode="Markdown")

bot.polling(none_stop=True, interval=0)