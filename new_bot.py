from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import datetime

token="8ec04fd67f724010314ae7be4b84c8379556346e86dbf7139f69708f71a693c0feb6a31386dcd13966369"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

with open('dr.txt','r',encoding='utf-8') as filee:
    data2=filee.readlines()

def week():
    l=[]
    for b in range(1,8):
        a = datetime.date.today()
        bb = datetime.timedelta(days=b)
        cc = a+bb
        l.append(str(cc))
    l1=[i[5:7] for i in l]
    l2=[i[-2:] for i in l]
    dr=[i for i in data2 if i[-4:-2] in l1 and i[-7:-5] in l1]
    if dr==[]:
        return 'На этой неделе пока никто не родился, но есть шанс это исправить)\nСвободен сегодня вечером?'
    else:
        return ''.join(dr)

def dr(m):
    mon={"январь":'01','февраль':'02','март':"03",'апрель':'04','май':'05','июнь':'06','июль':'07','август':'08','сентябрь':'09',"октябрь":'10','ноябрь':'11','декабрь':'12'}
    L=[i for i in data2 if i[-3:-1]==mon.get(m)]
    if L==[]:
        return 'В этом месяце пока никто не родился, но есть шанс это исправить)\nСвободен сегодня вечером?'
    else:
        return ''.join(L)


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать' or response=='на неделю' or response=='все' or response=='январь' or response=='февраль' or response=='март' or response=='апрель' or response=='май' or response=='июнь' or response=='июль' or response=='август' or response=='сентябрь' or response=='октябрь' or response=='ноябрь' or response=='декабрь':

        keyboard.add_button('Дни Рождения', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)


    elif response == 'привет':
        keyboard.add_button('начать', color=VkKeyboardColor.POSITIVE)

    elif response=='дни рождения':
        keyboard.add_button('На месяц',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('На неделю',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Все',color=VkKeyboardColor.PRIMARY)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    elif response=='на месяц':
        keyboard.add_button('Январь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Февраль',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Март',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Апрель',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Май',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Июнь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Июль',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Август',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Сентябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Октябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Ноябрь',color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Декабрь',color=VkKeyboardColor.PRIMARY)


    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)

            elif response == "начать":
                send_message(vk_session, 'user_id', event.user_id, message= 'Тестовые команды',keyboard=keyboard)

            elif response=='закрыть':
                send_message(vk_session, 'user_id', event.user_id, message='Закрыть',keyboard=keyboard)

            elif response=='дни рождения':
                send_message(vk_session,'user_id',event.user_id,message='Выбери нужный вариант',keyboard=keyboard)

            elif response=='на месяц':
                send_message(vk_session,'user_id',event.user_id,message='Выбери нужный месяц',keyboard=keyboard)

            elif response=='на неделю':
                send_message(vk_session,'user_id',event.user_id,message=week(),keyboard=keyboard)

            elif response=='все':
                send_message(vk_session,'user_id',event.user_id,message=''.join(data2),keyboard=keyboard)

            elif response=='январь' or response=='февраль' or response=='март' or response=='апрель' or response=='май' or response=='июнь' or response=='июль' or response=='август' or response=='сентябрь' or response=='октябрь' or response=='ноябрь' or response=='декабрь':
                send_message(vk_session, 'user_id', event.user_id, message=dr(response), keyboard=keyboard)
