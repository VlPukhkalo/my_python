import telebot
import config
import json
from telebot import types

bd={"Петухова Мария":"19.02","Шихаев Мурад ":"22.02","Юманов Сергей ":"23.02",
"Малышев Андрей ":"24.02","Косованов Валерий ":"14.03","Поздняков Максим ":"21.03",
"Пименова Таисия":"01.05","Майко Максим":"14.05","Постольник Роман":"02.06",
"Поташев Игорь":"12.06","Газимзянов Динар":"15.06","Рослая Ирина":"26.06",
"Дроздова Татьяна":"11.08","Калмыков Максим":"11.08","Пухкало Владислава":"28.08",
"Смирнов Артем":"11.09","Костыра Екатерина":"10.10","Максименко Николай":"10.10",
"Евдокимова Анастасия":"20.10","Кущенко Иван":"28.10","Борисова Марина":"04.11",
"Попова Софья":"21.12","Бронников Егор":"26.12"}

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message( message.chat.id, 'Привет!\n/birthday - узнай, когда День Рождения у кента!\n')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "birthday":
        bot.send_message(call.message.chat.id, 'Введи фамилию и имя!')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/birthday":
        bot.send_message(message.from_user.id,'Набери фамилию и имя солнышка!')
    else:
        bot.send_message(message.from_user.id, "Это солнышко празднует День Рождения "+bd.get(message.text,'не знаю когда'))

bot.polling(none_stop=True,interval=0)
